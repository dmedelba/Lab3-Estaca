import re
import string

libros = ['frankenstein.txt', 'moby_dick.txt', 'modest_proposal.txt', 
          'jekyll_hyde.txt', 'two_cities.txt', 'pride_prejudice.txt', 
          'beowulf.txt', 'dracula.txt', 'metamorphosis.txt', 'ulysses.txt']

# Armado corpus
output = open('./corpus.txt', 'w')
for libro in libros:
    archivo = open('./libros/'+libro, 'r')
    for linea in archivo:
        # Saltarse lineas en blanco
        if not linea.strip():
            continue
        # Reemplazar símbolos para dejar solo palabras y dejar en minúsculas
        corpus = linea.lower()
        # Filtrar guiones
        corpus = re.sub('-', ' ', corpus)
        # Permitir solo alfabeto y espacios en blanco
        allow = string.ascii_lowercase + ' ' + '\t' + '\n'
        corpus = re.sub('[^%s]' % allow, '', corpus)
        output.write(corpus)
    archivo.close()
output.close()