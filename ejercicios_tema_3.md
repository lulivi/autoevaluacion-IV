# Ejercicios propuestos del tema 3

## Índice
<!-- TOC depthFrom:3 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Ejercicio 1](#ejercicio-1)
- [Ejercicio 2 y 3](#ejercicio-2-y-3)
- [Ejercicio 4](#ejercicio-4)
- [Ejercicio 5 y 6](#ejercicio-5-y-6)
	- [Pruebas en local](#pruebas-en-local)
	- [Crear una nueva aplicación de heroku](#crear-una-nueva-aplicación-de-heroku)
	- [Nombre de la aplicación](#nombre-de-la-aplicación)
	- [Desplegado automático con github](#desplegado-automático-con-github)
	- [Fin!](#fin)

<!-- /TOC -->

### Ejercicio 1
**Darse de alta en algún servicio PaaS tal como Heroku, zeit, BlueMix u OpenShift.**

El primer servicio que he elegido ha sido [Heroku](https://www.heroku.com/).

Nos [creamos una cuenta](https://signup.heroku.com/) introduciendo nuestos datos:

![Singup](./img/t3-ej1-singup.png)

Elegimos el lenguage principal de nuestra aplicación:

![Select app](./img/t3-ej1-select_app.png)

Y seguimos la guía hasta el despliegue de la aplicación:

![Steps](./img/t3-ej1-steps.png)

### Ejercicio 2 y 3
**Realizar una app en express (o el lenguaje y marco elegido) que incluya variables como en el caso anterior.**

Para estos ejercicios he elegido un repositorio que ya tenía, [hitos-iv](https://github.com/lulivi/hitos-iv).

### Ejercicio 4
**Crear pruebas para las diferentes rutas de la aplicación.**

Los tests para la aplicación se pueden encontrar en la [carpeta de tests](https://github.com/lulivi/hitos-iv/blob/master/tests/test_hug_hitos_iv.py).

### Ejercicio 5 y 6
**Instalar y echar a andar tu primera aplicación en Heroku.**

Voy a utilizar la aplicación del ejercicio 2, hecha para hitos anteriores.

Para utilizar un repositorio de github y que se despliegue automáticamente la aplicación cada vez que hacemos un push a master, hay que seguír los siguientes pasos.

#### Pruebas en local

Para probar en local antes de conectar el repositorio con github, podemos utilizar el comando

    $ heroku local

Esto ejecutará los comandos proporcionados en el archivo Procfile obteniendo esta salida:

![Heroku local](./img/t3-ej5-heroku_local.png)

Entonces, accediendo a `localhost:5000` o `0.0.0.0:5000` veremos las salidas de a aplicación.

#### Crear una nueva aplicación de heroku

Nos dirigimos a [nuestro dashboard](https://dashboard.heroku.com/apps) y clicamos en nueva aplicación:

![Nueva Aplicación](./img/t3-ej2-new_app.png)

#### Nombre de la aplicación

Introducimos el nombre de nuestra aplicación (en blanco si queremos que nos de un nombre heroku):

![Nombre](./img/t3-ej2-app_name.png)

#### Desplegado automático con github

Finalmente seleccionamos como método de desplegado `github` y clicamos el desplegado automático:

![Desplegado automático](./img/t3-ej2-auto_deploy.png)

#### Fin!

Puedes acceder a la [aplicación de hitos](https://hitos-iv.herokuapp.com/) y hacer peticiones get a las siguientes rutas:

- `/` - Devolverá un OK
- `/all` - Mostrará el contenido del archivo [hitos.json](https://github.com/lulivi/hitos-iv/blob/master/data/hitos.json)
- `/get/{id}` - Mostará el contenido del hito indicado
- `/number` - Mostrará el número de hitos
