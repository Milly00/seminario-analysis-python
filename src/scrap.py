from apify_client import ApifyClient
import pandas as pd
from pysentimiento import create_analyzer

import json

import re
#nltk.download('vader_lexicon') 
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
import datetime
import os
from dotenv import load_dotenv
load_dotenv()
class Scrap():

    def __init__(self) -> None:
        self.api_key = os.getenv('API_KEY_APIFY')
        self.analyzer = create_analyzer(task="sentiment", lang="es")
        self.sentiment = create_analyzer(task="emotion",lang = "es")
    
    #Agregar variable de retorno
    def loadData(self,url_publicacion):
        # Initialize the ApifyClient with your API token
        posts = []

        try:
            client = ApifyClient(self.api_key)
        
            #Creamos un array vacio que contendra los datos brutos
            #serie = []
            # Prepare the actor input
            run_input = {
                "directUrls": [
                    url_publicacion,
                ],
                "resultsLimit": 100,
            }

            # Run the actor and wait for it to finish
            run = client.actor("apify/instagram-comment-scraper").call(run_input=run_input)

            # Fetch and print actor results from the run's dataset (if there are any)
            try:
                for item in client.dataset(run["defaultDatasetId"]).iterate_items():
                    #Obtenemos el texto del comentario
                    text_comment = self.remove_emoji(item['text'])
                    patron = r'@\w+\s?'
                    text_without_mencion =  re.sub(patron,"", text_comment)
                    #@[A-Za-z0-9_]+
                    if text_without_mencion != '' and len(text_without_mencion) > 15:
                        analysis_res = self.analyzer.predict(text_comment)
                        emotion = self.sentiment.predict(text_comment)
                        #print(analysis_res)
                        score = self.calculateScore(analysis_res.probas,analysis_res.output)

                        temporal = {"id_comentario": item['id'],"likes": item["likesCount"],"original_texto": text_without_mencion,"puntuacion": score,"fecha": str(item["timestamp"]),"etiqueta": analysis_res.output , "res_analisis": analysis_res.probas , "emocion": emotion.output , "res_emocion": emotion.probas}
                        posts.append(temporal)

                return posts
            except ValueError as ve:
                print("Los datos a evaluar no tienen un formato válido")
        except ValueError as ve:
                print("Ha ocurrido un error al realizar el analisis, intente de nuevo")
        

    #Agregar variable de retorno
    def loadDataTwitter(self,url_publicacion):
        # Initialize the ApifyClient with your API token
        posts = []
        try:
            client = ApifyClient(self.api_key)
            #Creamos un array vacio que contendra los datos brutos
            #serie = []
            # Prepare the actor input
            run_input = {
            "startUrls": [{ "url": url_publicacion }],
            "tweetsDesired": 100,
            }

            # Run the actor and wait for it to finish
            run = client.actor("quacker/twitter-scraper").call(run_input=run_input)
            try:
                # Fetch and print actor results from the run's dataset (if there are any)
                for item in client.dataset(run["defaultDatasetId"]).iterate_items():
                    #print(item)
                    #Obtenemos el texto del comentario
                    text_comment = self.remove_emoji(item['full_text'])
                    patron = r'@\w+\s?'
                    text_without_mencion =  re.sub(patron,"", text_comment)
                    if text_without_mencion != '' and len(text_without_mencion) > 15:
                        analysis_res = self.analyzer.predict(text_comment)
                        emotion = self.sentiment.predict(text_comment)
                        score = self.calculateScore(analysis_res.probas,analysis_res.output)
                        temporal = {"id_comentario": item['conversation_id'],"likes": item["favorite_count"],"original_texto": text_without_mencion,"puntuacion": score,"fecha": str(item["created_at"]),"etiqueta": analysis_res.output , "res_analisis": analysis_res.probas , "emocion": emotion.output , "res_emocion": emotion.probas}
                        posts.append(temporal)

                return posts
            except:
                print("Los datos a evaluar no tienen un formato válido")
        except:
            print("Ha ocurrido un error al realizar el analisis, intente de nuevo")
        

    def calculateScore(self,data,label):
        lista = list(data.values())
        max = 0
        #print(lista)
        try:
            for i in lista:
                #print(i)
                if(max < i):
                    max = i
            
            if(label == 'NEG'):
                max = max * -1
        except:
            max = 0
        return max

    def analysisSentiment(self,data):
        analysis = {}
        try:
            #Inicializamos la instancia
            sid = SentimentIntensityAnalyzer()
            #Calculamos la polaridad
            analysis = sid.polarity_scores(data)
            analysis = analysis
        except: 
            print("Ha ocurrido un error al analizar el tetxo")
        finally:
            return analysis
  
    def generateStatistic(self,data):
        #puntuacion,etiqueta,emocion,anger,disgust,fear
        #[puntuacion,etiqueta,emocion,anger]
        #lo otro buscarlo dentro del objeto res_emocion
        transform_data = []
        #datapy = json.loads(data)
        print('generate',data)
        
        for item in data:
            #anger, disgust  = data.res_emocion
            transform_data.append({ "fecha": item['fecha'], "puntuacion": item['puntuacion'], "etiqueta": item['etiqueta'], "emocion": item['emocion'], "likes": item['likes'], "anger": item['res_emocion']['anger'], "disgust": item['res_emocion']['disgust'], "fear": item['res_emocion']['fear'], "joy": item['res_emocion']['joy'], "others": item['res_emocion']['others'], "sadness": item['res_emocion']['sadness'], "surprise": item['res_emocion']['surprise']})
        print('transform',transform_data)
        return transform_data

    
    def remove_emoji(self,string):

        try:
            emoji_pattern = re.compile("["
                                        u"\U0001F600-\U0001F64F"  # emoticons
                                        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                        u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                        u"\U00002500-\U00002BEF"  # chinese char
                                        u"\U00002702-\U000027B0"
                                        u"\U00002702-\U000027B0"
                                        u"\U000024C2-\U0001F251"
                                        u"\U0001f926-\U0001f937"
                                        u"\U00010000-\U0010ffff"
                                        u"\u2640-\u2642"
                                        u"\u2600-\u2B55"
                                        u"\u200d"
                                        u"\u23cf"
                                        u"\u23e9"
                                        u"\u231a"
                                        u"\ufe0f"  # dingbats
                                        u"\u3030"
                                        u"\u002c"
                                        u"\u002e"
                                        u"\u0022"
                                        u"\u0040"
                                        "]+", flags=re.UNICODE)
            return emoji_pattern.sub(r'', string)
        except:
            print("No se pudo remover el caracter")

    def totalData(seld, data):
        total = len(data)
        return total
if __name__=="__main__":
    cls = Scrap()
    #title = "https://www.instagram.com/p/"
    #cls.loadData('unicor_sexy',title,'https://www.instagram.com/p/CpwLdMOA5us/')