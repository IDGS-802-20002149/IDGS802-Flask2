from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField 
from wtforms import EmailField, PasswordField, TextAreaField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula = StringField('Matricula',
        [validators.DataRequired(message='La matricula es requerida')])
    nombre = StringField('Nombre',
        [validators.DataRequired(message='Falta de ingresar un dato')],
        [validators.length(min=5, max=15, message='Ingresa una cadena entre 5 y 15 caracteres')])
    aPaterno = StringField('aPaterno')
    aMaterno = StringField('aMaterno')
    email = EmailField('Email')
    password = EmailField('Password')

class NumForm(Form):
    num = IntegerField('Numero') 
    numeros = IntegerField('numeros')