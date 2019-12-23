import re
import string

libros = ['frankenstein.txt', 'moby_dick.txt', 'modest_proposal.txt', 
          'jekyll_hyde.txt', 'two_cities.txt', 'pride_prejudice.txt', 
          'beowulf.txt', 'dracula.txt', 'metamorphosis.txt', 'ulysses.txt']

libros_es = ['divina_comedia.txt', 'don_quijote.txt', 'hamlet.txt', 'iliada.txt', 'odisea.txt']

def armarCorpus(libros, modo=0):
    # Armado corpus, modo 0 = inglés
    output = ''
    # Seleccionar archivos con los cuales trabajar
    if modo == 0:
        output = open('./corpus.txt', 'w')
    else:
        output = open('./corpus-es.txt', 'w')
    for libro in libros:
        archivo = ''
        if modo == 0:
            archivo = open('./libros/'+libro, 'r')
        else:
            archivo = open('./libros-es/'+libro, 'r')
        for linea in archivo:
            # Saltarse lineas en blanco
            if not linea.strip():
                continue
            # Reemplazar símbolos para dejar solo palabras y dejar en minúsculas
            corpus = linea.lower()
            # Filtrar guiones
            corpus = re.sub('-', ' ', corpus)
            if modo != 0:
                # Normalizar vocales con acento
                corpus = re.sub('á', 'a', corpus)
                corpus = re.sub('é', 'e', corpus)
                corpus = re.sub('í', 'i', corpus)
                corpus = re.sub('ó', 'o', corpus)
                corpus = re.sub('ú', 'u', corpus)
                # Normalizar eñes
                corpus = re.sub('ñ', 'n', corpus)
            # Permitir solo alfabeto y espacios en blanco
            allow = string.ascii_lowercase + ' ' + '\t' + '\n'
            corpus = re.sub('[^%s]' % allow, '', corpus)
            output.write(corpus)
        archivo.close()
    output.close()

armarCorpus(libros)
armarCorpus(libros_es, 1)