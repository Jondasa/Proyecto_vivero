Requisitos versiones del software:

- PostgreSQL >= 16
- asgiref >= 3.8.1
- Django >= 5.0.8
- psycopg >= 3.2.2
- psycopg-binary >= 3.2.2
- psycopg2 >= 2.9.9
- sqlparse >= 0.5.1
- typing_extensions >= 4.12.2
- tzdata >= 2024.1

Luego de tener instaladas las librerías necesarias.
Para ejecutar el proyecto localmente:

## Descargar el repositorio localmente

`git clone https://github.com/TheWizzard2/utp.git`

## Moverse al directorio del proyecto

`cd /utp`

## Ejecutar todas las migraciones

`python manage.py migrate`

## Ejecutar las pruebas en la aplicación vivero

`python manage.py test vivero`

## Ejecutar el proyecto

`python manage.py runserver`
