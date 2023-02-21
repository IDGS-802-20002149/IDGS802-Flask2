from flask import Flask, render_template
from flask import request
import forms

app=Flask(__name__)

@app.route("/Actividad1",methods=["GET", "POST"])
def Numero():
    form = forms.NumForm(request.form)
    if request.method == 'POST':
        opc = request.form.get('btnCalcular')
        if(opc == 'Generar'):
            return render_template("ActividadNumeros.html", form =form)
        elif (opc == 'Calcular'):
            menor = 0
            mayor = 0
            sum = 0
            numeros = request.form.getlist('numeros')
            
            for numero in numeros:
                if menor > numero:
                    menor = numero
                if mayor < numero:
                    mayor = numero
                sum += numero

            prom = sum/form.num.data
            return render_template("ActividadNumeros.html", form = form, menor = menor, mayor = mayor, promedio = prom)
        
    return render_template("ActividadNumeros.html", form = form)

if __name__ == "__main__":
    app.run(debug=True, port=3000)