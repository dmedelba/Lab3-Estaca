import re
import string

libros = ['frankenstein.txt', 'moby_dick.txt', 'modest_proposal.txt', 
          'jekyll_hyde.txt', 'two_cities.txt', 'pride_prejudice.txt', 
          'beowulf.txt', 'dracula.txt', 'metamorphosis.txt', 'ulysses.txt']

#libros = ['frankenstein.txt', 'moby_dick.txt', 'modest_proposal.txt', 
 #           'two_cities.txt', 'metamorphosis.txt']

output = open('./corpus.txt', 'w')
for libro in libros:
    archivo = open('./libros/'+libro, 'r')
    for linea in archivo:
        # Saltarse lineas en blanco
        if not linea.strip():
            continue
        # Reemplazar símbolos para dejar solo palabras
        corpus = linea.lower()
        allow = string.ascii_lowercase + ' ' + '\t' + '\n'
        corpus = re.sub('[^%s]' % allow, '', corpus)
        output.write(corpus)
    archivo.close()
output.close()

'''
# Realizar conteo
cuenta_palabras = dict()
nLineas = 0
for linea in corpus.split('\n'):
    nLineas += 1
    for palabra in linea.split():
        # Separar palabras de símbolos
        if not palabra.isalnum():
            continue
        # Estandarizar a minúsculas
        palabra = palabra.lower()
        if palabra in cuenta_palabras:
            cuenta_palabras[palabra] += 1
        else:
            cuenta_palabras[palabra] = 1'''