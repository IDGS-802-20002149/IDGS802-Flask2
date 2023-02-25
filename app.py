from flask import Flask, render_template
from flask import request, make_response, flash
from flask_wtf.csrf import CSRFProtect
import forms

app=Flask(__name__)
app.config['SECRET_KEY'] = "Esta es una clave encriptada"
csrf = CSRFProtect()

'''@app.before_request()
def before_request():
    print("num1")
'''
@app.route("/cookies", methods=["GET"])
def cookies():
    reg_user = forms.LoginForm(request.form)
    response = ''
    if request.method == 'POST' and reg_user.validate():
        user = reg_user.user.data
        passw = reg_user.passw.data
        datos = user + '@' + passw
        success_message='Bienvenido {}'.format(user)
        flash(success_message)

    response = make_response(render_template("cookies.html", form = reg_user))
    response.set_cookie('dato_user', datos)
    return response

@app.after_request
def after_request(response):
    print('num3')
    return response

@app.errorhandler(404)
def error(e):
    return render_template("404.html"), 404

@app.route("/saludo")
def saludo():
    valor_cookie = request.cookies.get('dato_user')
    nombre = valor_cookie.split('@')
    return render_template('saludo.html', nom = nombre[0])

@app.route("/formulario2",methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos",methods=["GET", "POST"])
def Alumno():
    alum_form = forms.UserForm(request.form)
    mat = ''
    nom = ''
    if request.method=='POST' and alum_form.validate():
        mat = alum_form.matricula.data
        nom = alum_form.nombre.data
        ap = alum_form.aPaterno.data
        am = alum_form.aMaterno.data
        em = alum_form.email.data
        pas = alum_form.password.data
    return render_template("Alumnos.html", form = alum_form, matricula = mat, nombre = nom)


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True, port=3000)