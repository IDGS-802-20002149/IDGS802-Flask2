from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField 
from wtforms import EmailField, PasswordField, TextAreaField, IntegerField
from wtforms import validators

class numForm(Form):
    numeros = IntegerField('numeros')
    inputNum = IntegerField('cantidad')

class dicForm(Form):
    eng = StringField('English')
    esp = StringField('Spanish')
    busqueda = StringField('Busqueda')