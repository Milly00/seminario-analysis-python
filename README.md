## Crear entorno virtual
    
    pip install virtualenv
    
## Nombrar el entorno virtual
Esto contendra las configuraciones de nuestro entorno virtual, le podemos dar el nombre de nuestra preferencia:

    virtualenv nombre

## Ejecutar entorno virtual
NOTA: "nombre" es el que le asignamos a nuestro entorno virtual

    .\nombre\Scripts\activate.bat

    o

    .\nombre\Scripts\activate

## Flask & PyMongo

Para crear la integración con Mongo DB

    pip install flask pymongo

Modulo que integra pymongo con flask (https://flask-pymongo.readthedocs.io/en/latest/)

    pip install flask-pymongo

    pip install flask-cors

## Waitress

    pip install waitress
## Apify

Se encarga de realizar el scrapper

    pip install apify-client

## Pandas

    pip install pandas

## Deep translator

   pip install deep-translator

## Nltk
    
    pip install nltk

## python-dotenv

    pip install python-dotenv

## py-sentimiento

    pip install pysentimiento

## Pytest
    pip install -U pytest

## pysentimiento

    pip install pysentimiento

## Estructura

    src: Archivos de la api
    venv: Archivos del entorno virtual

## Run API
    python src/app.py

