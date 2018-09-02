# -*- coding: utf-8 -*-
import numpy as np
from unidecode import unidecode

import pickle

from sklearn.ensemble import RandomForestClassifier,ExtraTreesClassifier,VotingClassifier

from flask import Flask

from flask import Flask, render_template, flash, request
from form import *



import re
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
# first we should load the embedding of  words in order to take the vector for each word
with open('word_embddings.pickle', 'rb') as handle:
    word_embddings = pickle.load(handle)







@app.route("/", methods=['GET', 'POST'])
def main_app():
    form = ReusableForm(request.form)

    if request.method == 'POST':
        name = request.form['name']

        if form.validate():
          flash(main(name))
        else:
            flash('Please enter a text')

    return render_template('index.html', form=form)




def tokenization(filename1,filename2):
    isim_dict={}
    yer_dict = {}
    # open the yer file
    with open(filename1, "r") as f:
        for yer in f:
            yer = yer.strip()
            yer = re.sub(" \d+", "  ", yer)
            pattern = r"[{}]".format(",.;")
            yer = re.sub(pattern, "", yer)
            yer_dict[yer]='yer'
    # open isim file
    with open(filename2, "r") as f:
        for isim in f:

            isim = isim.strip()
            isim = re.sub(" \d+", "  ", isim)
            pattern = r"[{}]".format(",.;")
            isim = re.sub(pattern, "", isim)
            isim_dict[isim] ='isim'
    # Join the two dicts
    joind_data = dict(yer_dict.items() + isim_dict.items())
    return joind_data


def build_data(joind_data):
    X_train = []
    labels = []
    # first we should load the embedding of  words in order to take the vector for each word
    with open('word_embddings.pickle', 'rb') as handle:
        word_embddings = pickle.load(handle)

    for word, label in joind_data.items():
        if word in word_embddings:
            word_embeddings = word_embddings[word]
            labels.append(label)

            X_train.append(word_embeddings)
    return X_train,labels


def train_data(X_train,label):
    rnd_clf_1 = RandomForestClassifier(random_state=0)
    extra_clf_1 = ExtraTreesClassifier(random_state=0)
    voting_clf = VotingClassifier(estimators=[('rf', rnd_clf_1), ('et', extra_clf_1)], voting='soft')
    voting_clf.fit(X_train, label)
    return voting_clf

def predict(weights,text):
    words=[]
    for word in text:
        word=word.title()
        word=word.encode("utf8")
        if word in word_embddings:
            word_embeddings = word_embddings[word]
            word_embeddings=np.array(word_embeddings)
            y_pred = weights.predict(word_embeddings.reshape(1,-1))
            y_pred_proba = weights.predict_proba(word_embeddings.reshape(1,-1))
            max_pred=max(max(y_pred_proba))
            if max_pred >=0.6:
                word=unicode(''.join(chr(ord(c)) for c in word).decode('utf8'))
                word=unidecode(word)
                words.append((word,y_pred[0]))
                words_list=set(words)
    return words_list

def input_tokenization(text):
    text = re.split("; |, |\*|\n|'| ", text)

    return text


def main(text):
    text=input_tokenization(text)
    joind_data=tokenization('yer.txt','isim.txt')
    X_train, labels=build_data(joind_data)
    voting_clf=train_data(X_train, labels)
    finalResult=predict(voting_clf,text)
    return finalResult



if __name__ == "__main__":
    app.run()