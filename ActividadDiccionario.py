from flask import Flask, render_template
from flask import request
import forms2

app=Flask(__name__)

@app.route("/Actividad2", methods=['GET','POST'])
def Diccionario():
    form = forms2.dicForm(request.form)
    sought = 'No encontrado'
    if request.method == 'POST' and form.validate():
        accion = request.form.get('button')
        if accion == 'Guardar':
            eng = request.form.get('eng')
            esp = request.form.get('esp')
            dic = open('Diccionario.txt','a')
            linea = str(eng).upper()+':'+str(esp).upper() + '\n'
            dic.write(linea)
            dic.close()
        elif accion == 'Buscar': 
            search = request.form.get('busqueda').upper()
            opc = request.form.get('rbtnOpcion')
            dic = open('Diccionario.txt','r')
            palabras = dic.readlines()
            if opc == '1':
                for palabra in palabras:
                    arreglo = palabra.split(':')
                    if arreglo[0] == search:
                        sought = arreglo[1]
            elif opc == '2':
                for palabra in palabras:
                    texto = palabra.replace('\n','')
                    arreglo = texto.split(':')
                    if arreglo[-1] == search:
                        sought = arreglo[0]
                        print(sought)
            dic.close()

    return render_template('ActividadDiccionario.html', form=form, sought = sought)

if __name__ == "__main__":
    app.run(debug=True, port=3000)