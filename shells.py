#!usr/bin/python
#en comentarios esta la implementacion con diccionario

fd = open('/etc/passwd', 'r')
lineas = fd.readlines()
fd.close
#dicc = {}

for linea in lineas:
    linea_div = linea.split(':')
    username = linea_div[0]
    shell = linea_div[-1][:-1] #con esto quitamos el /n
    #dicc[username] = shell
    print username, "utiliza", shell
    #print dicc["root"]
    
print "En esta maquina hay", len(lineas), "usuarios"
#print "En esta maquina hay", len(dicc), "usuarios"

#para excepciones:
#try:
#   print dicc["imaginario"]
#except KeyError:    #solo salta con errores KeyError
#   print "Usuario imaginario no existe"
