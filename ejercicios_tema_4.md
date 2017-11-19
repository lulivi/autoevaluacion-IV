# Ejercicios propuestos del tema 4

## Índice

<!-- TOC depthFrom:3 depthTo:6 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Ejercicio 1](#ejercicio-1)
- [Ejercicio 2: creación y ejecución de contenedores](#ejercicio-2-creación-y-ejecución-de-contenedores)
- [Ejercicio 3: Docker](#ejercicio-3-docker)
- [Ejercicio 4: Instalación de imágenes](#ejercicio-4-instalación-de-imágenes)
	- [Parte 1: Imagenes adicionales](#parte-1-imagenes-adicionales)
	- [Parte 2: Imagen con MongoDB](#parte-2-imagen-con-mongodb)
- [Ejercicio 5: Instalación de servicios](#ejercicio-5-instalación-de-servicios)

<!-- /TOC -->

### Ejercicio 1
**Instala LXC en tu versión de Linux favorita. Normalmente la versión en desarrollo, disponible tanto en GitHub como en el sitio web está bastante más avanzada; para evitar problemas sobre todo con las herramientas que vamos a ver más adelante, conviene que te instales la última versión y si es posible una igual o mayor a la 1.0.**

Buscamos el paquete con el gestor pacman:

	$ pacman -Ss lxc
	community/clxclient 3.9.0-2
			C++ wrapper library around the X Window System API
	community/lxc 1:2.1.1-1
			Linux Containers
	community/lxcfs 2.0.7-1
			FUSE filesystem for LXC

E instalamos el segundo paquete:

	$ sudo pacman -S lxc

### Ejercicio 2: creación y ejecución de contenedores
**Crear y ejecutar un contenedor basado en tu distribución y otro basado en otra distribución, tal como Fedora. Nota En general, crear un contenedor basado en tu distribución y otro basado en otra que no sea la tuya.**

Comandos principales de lxc:

- `$ sudo lxc-list -f`: muestra los contenedores instalados en el sistema.
- `$ sudo lxc-start -n <nombre_conenedor>`: levantar un contenedor.
- `$ sudo lxc-stop -n <nombre_contenedor>`: parar un contenedor.
- `$ sudo lxc-attach -n <nombre_contenedor>`: empezar un proceso dentro de un contenedor.

Para poder crear un contenedor de arch necesitamos instalar el paquete `arch-install-scripts`.

Posteriormente escribimos:

	$ sudo lxc-create -t ubuntu-cloud -n nubecilla
	$ sudo lxc-create -t archlinux -n arch-lxc

Para comprobar que todo está correcto:

	$ sudo lxc-ls -f
	NAME      STATE   AUTOSTART GROUPS IPV4 IPV6
	arch-lxc  RUNNING 0         -      -    -
	nubecilla RUNNING 0         -      -    -

Tambien podemos monitorizarlos por LXC Web Panel:

![lxc-web-panel](./img/t4-ej2-lxc_web_panel.png)

### Ejercicio 3: Docker
**Instalar docker.**

Como en el primer ejercicio, usamos el gestor de paquetes pacman:

	$ sudo pacman -S docker

### Ejercicio 4: Instalación de imágenes
#### Parte 1: Imagenes adicionales
**Instalar a partir de docker una imagen alternativa de Ubuntu y alguna adicional, por ejemplo de CentOS.**
#### Parte 2: Imagen con MongoDB
**Buscar e instalar una imagen que incluya MongoDB.**


### Ejercicio 5: Instalación de servicios
**Crear un usuario propio e instalar alguna aplicación tal como nginx en el contenedor creado de esta forma, usando las órdenes propias del sistema operativo con el que se haya inicializado el contenedor.**

### Ejercicio 6: Imagen persisitente
**Crear a partir del contenedor anterior una imagen persistente con commit.**


### Ejercicio 7: Dockerfile
**Crear un Dockerfile para el servicio web que se ha venido desarrollando en el proyecto de la asignatura.**


### Ejercicio 8: Desplegado
**Desplegar un contenedor en alguno de estos servicios, de prueba gratuita o gratuitos.**
