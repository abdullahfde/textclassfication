from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


class ReusableForm(Form):
    name = StringField('Text:', validators=[validators.required()])