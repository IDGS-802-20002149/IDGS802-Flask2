from flask import Flask, render_template
from flask import request
import forms

app=Flask(__name__)

@app.route("/formulario2",methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos",methods=["GET", "POST"])
def Alumno():
    alum_form = forms.UserForm(request.form)    
    alum_form =  forms.UserForm.matricula
    alum_form =  forms.UserForm.nombre
    alum_form =  forms.UserForm.aPaterno
    alum_form =  forms.UserForm.aMaterno
    alum_form =  forms.UserForm.email
    return render_template("Alumnos.html")


if __name__ == "__main__":
    app.run(debug=True, port=3000)