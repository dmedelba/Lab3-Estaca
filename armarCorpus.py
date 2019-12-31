import re
import string

libros = ['frankenstein.txt', 'moby_dick.txt', 'modest_proposal.txt', 
          'jekyll_hyde.txt', 'two_cities.txt', 'pride_prejudice.txt', 
          'beowulf.txt', 'dracula.txt', 'metamorphosis.txt', 'ulysses.txt']

libros_es = ['divina_comedia.txt', 'don_quijote.txt', 'hamlet.txt', 'iliada.txt', 'odisea.txt',
            'juan_tenorio.txt', 'quimera.txt', 'perfecta.txt', 'clasicos.txt', 'cuentos.txt']

libro = ["two_cities.txt"]

def armarCorpus(libros, modo=0):
    # Armado corpus, modo 0 = inglés
    output = ''
    # Seleccionar archivos con los cuales trabajar
    if modo == 0:
        output = open('./corpus.txt', 'w')
    else:
        output = open('./corpus-es.txt', 'w')
    skip=1
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
            # Filtrar partes gutenberg
            if skip:
                if re.match(".*(start).*(project gutenberg).*", corpus) != None:
                    skip = 0
                continue
            elif re.match(".*(end).*(project gutenberg).*", corpus) != None:
                skip = 1
                continue
            output.write(corpus)
        archivo.close()
    output.close()

# Función para armar corpus (para b.1) con menos filtros, para una mejor identificación de tags
def armarCorpusB(libros, modo=0):
    # Armado corpus, modo 0 = inglés
    output = ''
    # Seleccionar archivos con los cuales trabajar
    if modo == 0:
        output = open('./corpus-libro.txt', 'w')
    else:
        output = open('./corpus-es.txt', 'w')
    skip=1
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
            # Filtrar partes gutenberg
            if skip:
                if re.match(".*(start).*(project gutenberg).*", corpus) != None:
                    skip = 0
                continue
            elif re.match(".*(end).*(project gutenberg).*", corpus) != None:
                skip = 1
                continue
            output.write(corpus)
        archivo.close()
    output.close()

armarCorpus(libros)
armarCorpus(libros_es, modo=1)
armarCorpusB(libro)