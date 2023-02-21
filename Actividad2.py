alumnos = {'Matricula':'12345', 'Nombre':'Mario', 'Apellidos':'Lopez', 'correo':'123@123'}

f = open('alumnos2.txt','a')
for items in alumnos:
    f.write (str(items)+':')
    f.write(str(alumnos[items])+'\n')
f.close()
