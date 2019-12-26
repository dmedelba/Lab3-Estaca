# Laboratorio 3 - Estadística Computacional

## Instrucciones:
El presente laboratorio se desorrollo en python 3.
Se puede ejecutar con `jupyter lab .` desde consola, estando dentro de la carpeta.
* Es necesario tener instalado los siguientes paquetes en nuestro entorno Python:
```
    pip install matplotlib
    pip install pandas
    pip install numpy
    pip install random
```

## Indicaciones generales:
Los libros utilizados para el corpus en formato .txt fueron obtenidos del [proyecto gutenberg](https://www.gutenberg.org/browse/scores/top), en donde se trabajó con los siguientes libros para las partes 1 y 2, los cuales para la ejecución deben estar en la carpet `./libro`:
- Frankenstein; Or, The Modern Prometheus by Mary Wollstonecraft Shelley - frankenstein.txt
- Moby Dick; Or, The Whale by Herman Melville - moby_dick.txt
- A Modest Proposal by Jonathan Swift - modest_proposal.txt
- The Strange Case of Dr. Jekyll and Mr. Hyde by Robert Louis Stevenson - jekyll_hyde.txt
- A Tale of Two Cities by Charles Dickens - two_cities.txt
- Pride and Prejudice by Jane Austen - pride_prejudice.txt
- Beowulf: An Anglo-Saxon Epic Poem by J. Lesslie Hall - beowulf.txt
- Dracula by Bram Stoker - dracula.txt
- Metamorphosis by Franz Kafka - metamorphosis.txt
- Ulysses by James Joyce - ulysses.txt
Generando el archivo: './corpus.txt'.

A su vez también se utilizó un listado de libros en español del mismo sitio para la parte 2, los cuales para la ejecución deben estar en la carpeta `./libros-es`:
- La Divina Comedia por Dante Alighieri - divina_comedia.txt
- Don Quijote por Miguel de Cervantes - don_quijote.txt
- Hamlet: Drama en cinco actos por William Shakespeare - hamlet.txt
- La Ilíada por Homero - iliada.txt
- La Odisea por Homero - odisea.txt
- Cuentos de Amor de Locura y de Muerte por Horacio Quiroga - cuentos.txt
- Cuentos Clásicos del Norte, Primera Serie por Edgar Allan Poe - clasicos.txt
- Don Juan Tenorio por José Zorrilla - juan_tenorio.txt
- Doña Perfecta por Benito Pérez Galdós - perfecta.txt
- La Quimera por condesa de Emilia Pardo Bazán - quimera.txt
Generando el archivo: './corpus-es.txt'.

En el trabajo de la parte 1,d), también se utilizó el siguiente [listado de stopwords](http://xpo6.com/list-of-english-stop-words/), en el archivo `stop-word-list.csv` para el filtrado de las posibles soluciones, el cual debe estar en la carpeta raíz del notebook para su correcta ejecución.