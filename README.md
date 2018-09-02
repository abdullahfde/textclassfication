# Names and Places Recognition based pre trained Fasttext and ensemble learning.

# Method
- Collecting data from different websites which contains Turkish names and places by using beautiful soup python library.
 Then processing the data and clean it then stor it in text file. >>>isim.txt >>>yer.txt
- Installing pre trained fasttext model file for embeddings turkish words. 
- Tagging each name and place in my data to it's corresponding vector then saving it to Pickle file which called >> word_emeddings 

# Data Processing
- Load isim.txt then put in isim_dict
- Load yer.txt then put in yer_dict then join the two dicts
- Load the word embeddings vectors pickle file
- Extract the word embedding vector vector for each word
- Prepare the X_train and y_train 

# Classfication 

- Using ensemble learning (RandomForest and ExtraTrees) 


# Web Development
- Prepare a simple Html file >> index.html
- Develop the app

# Accuracy 
  94% 
  
# Future
This work can imporved :
- Collect more data
- Extand the word_emddings file to inculde all words 
- Apply RNN



*Note I couldn't use Docker becuase docker doesn't support all Windows version, it requires Windows Pro

