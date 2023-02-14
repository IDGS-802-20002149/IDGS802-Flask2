from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField, EmailField

class UserForm(Form):
    matricula = StringField('Matricula')
    nombre = StringField('Nombre')
    aPaterno = StringField('aPaterno')
    aMaterno = StringField('aMaterno')
    email = EmailField('Email')