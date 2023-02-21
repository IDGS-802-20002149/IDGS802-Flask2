'''
nombres = f.read()
print(nombres)

nombres2 = f.readline()
print(nombres2)

nombres2 = f.readlines()

f.close()

for items in nombres2:
    print(items, end='')
'''
f = open('alumnos.txt','w')
f.write('Hola mundo!!!')

f = open('alumnos.txt','a')
f.write('\nMario\n')
f.write('Pedro')