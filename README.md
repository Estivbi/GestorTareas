![captura de la web](https://github.com/user-attachments/assets/31c9f218-9487-4f8d-96f2-f2795b93c710)

# GestorTareas

GestorTareas es una aplicación web sencilla para la gestión de tareas (to-do list), desarrollada con **Flask** y **Python**. Permite crear, marcar como hechas y eliminar tareas, almacenando la información en una base de datos SQLite.

## Características principales

- Crear tareas nuevas.
- Marcar tareas como hechas o deshechas.
- Eliminar tareas.
- Interfaz web sencilla usando HTML y Flask.

## Estructura del proyecto

- `main.py`: Archivo principal de la aplicación Flask, define las rutas y la lógica principal.
- `db.py`: Configuración y manejo de la base de datos SQLite.
- `models.py`: Definición del modelo de datos para las tareas.
- `templates/`: Plantillas HTML para la interfaz de usuario.
- `static/`: Archivos estáticos como CSS o imágenes.
- `database/` y `identifier.sqlite`: Archivos relacionados con la base de datos y persistencia.

## Tecnologías utilizadas

- **Python 3**
- **Flask** para el backend web
- **SQLite** como base de datos
- **HTML** para la interfaz de usuario

## Instalación y uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Estivbi/GestorTareas.git
   cd GestorTareas
   ```
2. Instala las dependencias necesarias (asegúrate de tener `pip` y Python 3):
   ```bash
   pip install flask
   ```
3. Ejecuta la aplicación:
   ```bash
   python main.py
   ```
4. Abre tu navegador en `http://127.0.0.1:5000/` para comenzar a gestionar tus tareas.

## Contribución

¡Las contribuciones son bienvenidas! Puedes crear un fork y enviar un pull request.

## Licencia

Este proyecto actualmente no tiene una licencia especificada.

---

> _Repositorio creado por [Estivbi](https://github.com/Estivbi)_
