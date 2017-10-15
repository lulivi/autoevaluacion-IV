# Ejercicios propuestos del tema 2

## TOC
<!-- TOC depthFrom:3 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Ejercicio 1 y 2](#ejercicio-1-y-2)
- [Ejercicio 3](#ejercicio-3)
- [Ejercicio 4](#ejercicio-4)
	- [Python 2.7](#python-27)
		- [Crear Entorno](#crear-entorno)
	- [Python 3.6](#python-36)
		- [Crear entorno](#crear-entorno)
	- [Activado y desactivado del entorno](#activado-y-desactivado-del-entorno)

<!-- /TOC -->

### Ejercicio 1 y 2
**Hacer un pull request a este proyecto con tests adicionales, si es que faltan (en el momento que se lea este tema)**

Dado que no he usado demasiado go, y me manejo mejor en python, he creado un proyecto en python que simula la misma funcionalidad que [el proyecto en go](https://github.com/JJ/HitosIV). El repositorio [**se puede encontra aquí**](https://github.com/lulivi/hitos-iv).

### Ejercicio 3
**Convertir los tests unitarios anteriores con assert a programas de test y ejecutarlos desde mocha, usando descripciones del test y del grupo de test de forma correcta. Si hasta ahora no has subido el código que has venido realizando a GitHub, es el momento de hacerlo, porque lo vas a necesitar un poco más adelante.**

Como antes, como he utilizado python para los ejercicios anteriores, existe un paquete llamado [pocha](https://github.com/rlgomes/pocha) para hacer programas de tests. [**Aquí está el módulo de tests con pocha**](https://github.com/lulivi/hitos-iv/blob/master/tests/test_hitos_iv_pocha.py).

### Ejercicio 4
**Instalar alguno de los entornos virtuales de node.js (o de cualquier otro lenguaje con el que se esté familiarizado) y, con ellos, instalar la última versión existente, la versión minor más actual de la 4.x y lo mismo para la 0.11 o alguna impar (de desarrollo).**

Para la instalación de entornos virtuales de python con diferentes versiónes hay que hacer lo siguiente (he utilizado la versión 3.6 y 2.7):

#### Python 2.7

Para la versión 2.7 vamos a utilizar el paquete `virtualenv`:

    # pip2 install virtualenv

##### Crear Entorno

Para crear el entorno virtual se usa lo siguiente:

    $ virtualenv --python=python2.7 python-venv-2_7

#### Python 3.6

A partir de la versión 3.3 de python se recomienda usar `venv`:

    # pip3 install venv

##### Crear entorno

Utilizamos el siguiente comando para crear el entorno virtual

    $ python3.6 -m venv python-venv-3_6

#### Activado y desactivado del entorno

Entramos en la carpeta e iniciamos el entorno:

    $ cd python-venv-X_X
    $ source ./bin/activate

Comprobamos que efectivamente estamos ejecutando la versión 2.7 de python:

    $ python --version
    Python 2.7.14
    ó
    Python 3.6.2
