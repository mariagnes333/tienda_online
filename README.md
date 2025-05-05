# Proyecto Base de Tienda MVC con Flask

Este es un proyecto base para una tienda online utilizando el patrón de arquitectura **MVC** (Modelo-Vista-Controlador) y el framework **Flask**. El proyecto está configurado con una base de datos **SQLite** y contiene algunas rutas para gestionar productos.

## ¿Cómo descargar el proyecto?

### Opción 1: Descargar como archivo ZIP
1. Dirígete al [repositorio de GitHub](https://github.com/mariagnes333/tienda_online).
2. Haz clic en el botón verde que dice **Code**.
3. Selecciona la opción **Download ZIP**.
4. Extrae el archivo en una carpeta de tu elección.

### Opción 2: Clonar el repositorio con Git (recomendado si tienes experiencia con Git)
1. Asegúrate de tener instalado [Git](https://git-scm.com/).
2. Abre tu terminal (CMD o terminal de tu preferencia).
3. Ejecuta el siguiente comando para clonar el repositorio:
   ```bash
   git clone https://github.com/mariagnes333/tienda_online.git
4. Entra en la carpeta del proyecto:
	cd tienda_online

Requisitos

* Python 3.8 o superior.
* Flask.
* Flask-SQLAlchemy.
* Flask-Migrate.
* SQLite como base de datos (se configura automáticamente).

-- Instalación

1. Asegúrate de tener instalado Python.
2. Crea un entorno virtual (opcional pero recomendado):
	python -m venv venv

3. Activa el entorno virtual:
	.\venv\Scripts\activate

4. Instala las dependencias del proyecto:
	pip install -r requirements.txt

-- Configuración de la Base de Datos
1. Si es la primera vez que ejecutas el proyecto, debes inicializar la base de datos:
	python init_db.py

Esto creará las tablas necesarias en la base de datos tienda.db.

-- Ejecución del Proyecto
1. Inicia el servidor de desarrollo:
				python run.py

El servidor estará disponible en http://127.0.0.1:5000.

2. Abre tu navegador y visita la dirección mencionada. Verás la página de inicio de la tienda.

-- Estructura del Proyecto

* app/: Contiene todo el código de la aplicación.

	* models/: Contiene los modelos de datos.

	* routes/: Define las rutas de la aplicación (vistas y 	controladores).

	* templates/: Contiene las plantillas HTML.

* config.py: Archivo de configuración del proyecto.

* requirements.txt: Lista de dependencias necesarias para el proyecto.

* run.py: Script para iniciar la aplicación Flask.

-- ¿Cómo colaborar en el proyecto?

Si deseas realizar cambios en el proyecto, sigue estos pasos:

1. Haz un Fork del repositorio.

2. Clona tu fork localmente:
		git clone https://github.com/TU_USUARIO/tienda_online.git

3. Crea una nueva rama para tus cambios:
	git checkout -b nombre-de-tu-rama

4. Realiza tus cambios y haz commit:
	git add .
	git commit -m "Descripción de los cambios realizados"

5. Sube tus cambios a tu fork:
	git push origin nombre-de-tu-rama

Notas
Este es un proyecto educativo, por lo que está diseñado para ayudar a los estudiantes a entender el patrón MVC y cómo se utiliza en una aplicación web sencilla con Flask.

Si tienes dudas o problemas, no dudes en abrir un "issue" en el repositorio para que podamos ayudarte.

¡Feliz programación!



