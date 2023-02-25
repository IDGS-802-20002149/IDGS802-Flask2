from flask import Flask, render_template
from flask import request
from collections import Counter
import forms

app=Flask(__name__)

@app.route("/Actividad1", methods=['GET','POST'])
def Numeros():
    num_form= forms.numForm(request.form)
    if request.method=='POST':
        btn = request.form.get("btnCalcular")
        if btn == 'Generar':
            return render_template('ActividadNumeros.html',form=num_form)
        if btn == 'Calcular':
            numeros = request.form.getlist("numeros")
            mayor = 0 
            for num in numeros:
                if (int(num) > mayor):
                    mayor = int(num)

            menor = 0
            for num in numeros:
                if (int(num) < menor):
                    menor = int(num)

            for i in range(len(numeros)):
                numeros[i] = int(numeros[i])


            prom = 0
            prom = sum(numeros) / len(numeros)

            counter = Counter(numeros)
            resultados = counter.most_common()
            textoResultado = ''
            for r in resultados:
                if r[1] > 1:
                    textoResultado += '<p>El {0} se repite {1} veces</p>'.format(r[0], r[1])
            return render_template('ActividadNumeros.html',form=num_form, mayor=mayor, menor=menor, prom=prom, repetidos = textoResultado)
    return render_template('ActividadNumeros.html', form=num_form)

if __name__ == "__main__":
    app.run(debug=True, port=3000)