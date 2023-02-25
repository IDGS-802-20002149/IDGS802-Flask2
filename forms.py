from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField, RadioField 
from wtforms import EmailField, PasswordField, TextAreaField, IntegerField
from wtforms import validators 

def mi_validacion(Form, field):
    if len(field.data)==0:
        raise validators.ValidationError('El campo no tiene datos')

class UserForm(Form):
    matricula = StringField('Matricula',
        validators.DataRequired(message='La matricula es requerida'))
    nombre = StringField('Nombre',[
        validators.DataRequired(message='Falta de ingresar un dato'),
        validators.length(min=5, max=15, message='Ingresa una cadena entre 5 y 15 caracteres')])
    aPaterno = StringField('aPaterno', [mi_validacion])
    aMaterno = StringField('aMaterno')
    email = EmailField('Email')
    password = PasswordField('Password')

class LoginForm(Form):
    user = StringField('user',
        validators.DataRequired(message='El campo es requerido'))
    passw = StringField('passw',[
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=5, max=15, message='Ingresa una cadena entre 5 y 15 caracteres')])

class numForm(Form):
    numeros = IntegerField('numeros')
    inputNum = IntegerField('cantidad')

class dicForm(Form):
    eng = StringField('English', validators.DataRequired(message="Por favor ingresa la informacion completa"))
    esp = StringField('Spanish', validators.DataRequired(message="Por favor ingresa la informacion completa"))
    busqueda = StringField('Busqueda', validators.DataRequired(message="Por favor ingresa la informacion completa"))