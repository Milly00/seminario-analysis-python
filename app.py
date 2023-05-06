from flask import Flask, request,jsonify, Response
from flask_pymongo import PyMongo
from pymongo import MongoClient

from flask_cors import CORS
from src.scrap import Scrap #recordar instalar el paquete
import datetime

import pandas as pd

import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__) #Instancia de una app
#app.config['MONGO_URI']='mongodb://localhost:27017/seminario' #cadena de conexion
app.config['MONGO_URI']= os.getenv('MONGO_URI') #cadena de conexion
CORS(app)

mongo = PyMongo(app) #Pasamos la cadena de conexion para conectarnos a la BD

scrap =  Scrap()

@app.route('/')
def index():
    return jsonify({'hello': 'world'})

@app.route('/analysis', methods=['POST'])
def createPublication():

    try:
        print(request.json)
        profile_name = request.json['profile_name']
        name_post = request.json['name_post']
        #name_file = request.json['name_file']
        id_admin = request.json['id_admin']
        descripcion = request.json['descripcion']
        n_redsocial = request.json['n_redsocial']
        url_publicacion = request.json['url_publicacion']
        category = request.json['categoria']
        data = []
        if(n_redsocial == 'instagram'):
            data = scrap.loadData(url_publicacion)

        if(n_redsocial == 'twitter'):
            data = scrap.loadDataTwitter(url_publicacion)
        
        if profile_name and name_post  and id_admin and descripcion and n_redsocial and url_publicacion and category:
            #comentar el método en caso de que no haya conx con la BD
            
            id_p = savePublication(data, name_post,id_admin,descripcion,n_redsocial,url_publicacion,profile_name, category)
            #saveStatistic(data, name_post)
            response = jsonify({
            'message': 'Se ha registrado su publicación',
            'status': 200,
            'data': data,
            '_id' : str(id_p)
            })

            #Llamar el método de crear estadisticas
            return response
        else:
            return not_found()
    except Exception as err:
        print(err)
        return  service_error()

@app.route('/new-statistic', methods=['POST'])
def createStatistic():
    try:
        #print(request.json)
        id_publication = request.json['name_post']
        data = request.json['data']
        owner = request.json['owner']
        p_id = request.json['p_id']


        new_data = scrap.generateStatistic(data)
        #print('newdata:'+new_data)
        saveStatistic(id_publication, new_data,owner,p_id)
        
        res = {'ok': True, 'data': new_data}
        return res
        
    except Exception as err:
        print('Error createEst')
        print(err)
        return service_error()


def savePublication(data,id,id_admin,descripcion,n_redsocial,url_publicacion, autor,categoria):
        try:
            #Inicio con la BD
            #print(data)
            date = datetime.datetime.now()
            #data = scrap.analysisSentiment(url_publicacion)
            #print(data)
            res = mongo.db.publications.insert_one({"data": data , "createdAt": date,"pid": id,"uid": id_admin,"total_data": scrap.totalData(data), "description": descripcion,"social_network": n_redsocial, "url_publication": url_publicacion, "owner": autor,"category": categoria})
            print(res.inserted_id)
            return res.inserted_id
        except Exception as err:
            print('ERRROR saveP')
            print(err)
            return service_error()



def saveStatistic(id_publication, data,autor,p_id):
    try:
        #print(id_publication, data)
        date = datetime.datetime.now()
        data_matriz = []
        for value in data:
            element = [value['puntuacion'], value['etiqueta'], value['emocion'], value['likes'], value['fecha']]
            data_matriz.append(element)
        
        df_matriz = pd.DataFrame(data_matriz, columns=["Score", "Polarity", "Emotion", "Likes", "Date"])
        
        description = df_matriz.describe()
        polarity = df_matriz.Polarity.value_counts()
        count_emotions = df_matriz.Emotion.value_counts()
        
        description_db = description.to_json()
        polarity_db = polarity.to_json()
        count_emotions_db = count_emotions.to_json()

        
        mongo.db.statistics.insert_one({"pid": id_publication ,"p_id": p_id, "createdAt": date, "data": data, "description": description_db, "polarity": polarity_db, "count_emotions": count_emotions_db,"owner": autor})
        
    except Exception as err:
        print('ERROR saveStatistic')
        print(err)
        return service_error()



@app.errorhandler(404)
def not_found(error = None):
    response = jsonify({
        'message': 'Resource Not Found:' + request.url,
        'status': 404
    })

    response.status_code = 404
    return response

@app.errorhandler(500)
def service_error(error = None):
    response = jsonify({
        'message': 'Error:' + request.url,
        'status': 500
    })

    response.status_code = 500
    return response

#Si esta ejecutando el archivo como modulo principal ejecutar la app
if __name__ == "__main__":
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True,port=8000)
    app.config['TESTING'] = True
    app.config['DEBUG'] = True