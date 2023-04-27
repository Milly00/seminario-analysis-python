import pytest
from app import app as flask_app
import json
from flask import jsonify

@pytest.fixture
def app():
    yield flask_app
@pytest.fixture
def client(app):
    return app.test_client()

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = {'hello': 'world'}
    assert expected == json.loads(res.get_data(as_text=True))
    
def test_create_statistic(app,client):
    
    data = [
        {
            "autor": "omorong",
            "emocion": "others",
            "etiqueta": "NEU",
            "fecha": "2023-03-23T21:54:35.000Z",
            "id_comentario": "17987337898782222",
            "likes": 5,
            "original_texto": "El mismo la mando a retirarinfórmese mejor",
            "puntuacion": 0.7158522009849548,
            "res_analisis": {
                "NEG": 0.24275510013103485,
                "NEU": 0.7158522009849548,
                "POS": 0.04139270633459091
            },
            "res_emocion": {
                "anger": 0.006027688272297382,
                "disgust": 0.0026320628821849823,
                "fear": 0.0012701087398454547,
                "joy": 0.0017559657571837306,
                "others": 0.9814785718917847,
                "sadness": 0.004030308220535517,
                "surprise": 0.0028051796834915876
            }
        },
        {
            "autor": "sebastiangop9",
            "emocion": "others",
            "etiqueta": "NEG",
            "fecha": "2023-03-23T22:24:17.000Z",
            "id_comentario": "17949003698415777",
            "likes": 3,
            "original_texto": "El mismo la manda a retirar y dicen que derrota  medios desinformativos",
            "puntuacion": -0.8512487411499023,
            "res_analisis": {
                "NEG": 0.8512487411499023,
                "NEU": 0.14053119719028473,
                "POS": 0.008220069110393524
            },
            "res_emocion": {
                "anger": 0.02200777642428875,
                "disgust": 0.009237739257514477,
                "fear": 0.0007329530781134963,
                "joy": 0.003107023425400257,
                "others": 0.9584774374961853,
                "sadness": 0.0041982633993029594,
                "surprise": 0.0022388228680938482
            }
        },
        {
            "autor": "miladyssilgadoberna",
            "emocion": "anger",
            "etiqueta": "NEG",
            "fecha": "2023-03-23T22:26:51.000Z",
            "id_comentario": "18177696457257903",
            "likes": 5,
            "original_texto": "A algunos periodistas sólo les interesa es desprestigiar al gobierno Lo demuestra el titular",
            "puntuacion": -0.9649377465248108,
            "res_analisis": {
                "NEG": 0.9649377465248108,
                "NEU": 0.03019109182059765,
                "POS": 0.004871134180575609
            },
            "res_emocion": {
                "anger": 0.4808278977870941,
                "disgust": 0.046351201832294464,
                "fear": 0.0028394463006407022,
                "joy": 0.0033776757773011923,
                "others": 0.4447609782218933,
                "sadness": 0.02085951529443264,
                "surprise": 0.0009832822252064943
            }
        },
        {
            "autor": "laurenssofia",
            "emocion": "others",
            "etiqueta": "NEU",
            "fecha": "2023-03-23T22:52:59.000Z",
            "id_comentario": "18003096313636535",
            "likes": 0,
            "original_texto": "",
            "puntuacion": 0.5332097411155701,
            "res_analisis": {
                "NEG": 0.10260693728923798,
                "NEU": 0.5332097411155701,
                "POS": 0.3641832768917084
            },
            "res_emocion": {
                "anger": 0.0002733129367697984,
                "disgust": 0.00019974444876424968,
                "fear": 0.00023743190104141831,
                "joy": 0.0038081002421677113,
                "others": 0.9933227896690369,
                "sadness": 0.000551290693692863,
                "surprise": 0.0016073461156338453
            }
        },
        {
            "autor": "ilsegonzalezb",
            "emocion": "others",
            "etiqueta": "NEU",
            "fecha": "2023-03-23T22:56:52.000Z",
            "id_comentario": "18352896532007135",
            "likes": 0,
            "original_texto": "",
            "puntuacion": 0.5716180205345154,
            "res_analisis": {
                "NEG": 0.17449268698692322,
                "NEU": 0.5716180205345154,
                "POS": 0.253889262676239
            },
            "res_emocion": {
                "anger": 0.00041761892498470843,
                "disgust": 0.00031882073380984366,
                "fear": 0.00030432245694100857,
                "joy": 0.0038110516034066677,
                "others": 0.9923606514930725,
                "sadness": 0.0006436727126128972,
                "surprise": 0.002143942518159747
            }
        },
        {
            "autor": "markega65",
            "emocion": "others",
            "etiqueta": "NEG",
            "fecha": "2023-03-24T00:05:15.000Z",
            "id_comentario": "17950080095402724",
            "likes": 4,
            "original_texto": "Que retiren las otras también ",
            "puntuacion": -0.49712738394737244,
            "res_analisis": {
                "NEG": 0.49712738394737244,
                "NEU": 0.4763333201408386,
                "POS": 0.02653922326862812
            },
            "res_emocion": {
                "anger": 0.005566732957959175,
                "disgust": 0.0016382185276597738,
                "fear": 0.0003849536878988147,
                "joy": 0.018720747902989388,
                "others": 0.9667629599571228,
                "sadness": 0.0036658765748143196,
                "surprise": 0.0032604732550680637
            }
        },
        {
            "autor": "desantishector",
            "emocion": "anger",
            "etiqueta": "NEG",
            "fecha": "2023-03-24T01:33:50.000Z",
            "id_comentario": "18040066738439525",
            "likes": 0,
            "original_texto": "Por corructo y bandido",
            "puntuacion": -0.8314850330352783,
            "res_analisis": {
                "NEG": 0.8314850330352783,
                "NEU": 0.12590640783309937,
                "POS": 0.042608585208654404
            },
            "res_emocion": {
                "anger": 0.6300069689750671,
                "disgust": 0.3486669361591339,
                "fear": 0.003564197802916169,
                "joy": 0.004564029164612293,
                "others": 0.007445306051522493,
                "sadness": 0.0029172080103307962,
                "surprise": 0.002835409715771675
            }
        },
        {
            "autor": "dayrojsquitian",
            "emocion": "anger",
            "etiqueta": "NEG",
            "fecha": "2023-03-24T01:41:26.000Z",
            "id_comentario": "17974593344007261",
            "likes": 1,
            "original_texto": "Que asco de periodistas  el mismo Pacto Histórico lo mando a retirar",
            "puntuacion": -0.9466223120689392,
            "res_analisis": {
                "NEG": 0.9466223120689392,
                "NEU": 0.048930682241916656,
                "POS": 0.004447069950401783
            },
            "res_emocion": {
                "anger": 0.5937942862510681,
                "disgust": 0.3957666754722595,
                "fear": 0.0020637211855500937,
                "joy": 0.0007403442868962884,
                "others": 0.0028940378688275814,
                "sadness": 0.0037623574025928974,
                "surprise": 0.0009786152513697743
            }
        },
        {
            "autor": "luzmarina.nieto.94849",
            "emocion": "others",
            "etiqueta": "NEG",
            "fecha": "2023-03-24T02:21:42.000Z",
            "id_comentario": "17968611599100212",
            "likes": 0,
            "original_texto": "miladyssilgadoberna aún no aceptan que es el presidente que ganó por mayoría de votos tienen más tiempo para sufrir y Petro para ejercer su cargo Dios  bendiga a Colombia les direccione cada proyecto que venga para bien nuestro",
            "puntuacion": -0.8362652659416199,
            "res_analisis": {
                "NEG": 0.8362652659416199,
                "NEU": 0.13309462368488312,
                "POS": 0.03064008243381977
            },
            "res_emocion": {
                "anger": 0.03952636197209358,
                "disgust": 0.014227250590920448,
                "fear": 0.0027497762348502874,
                "joy": 0.02084825374186039,
                "others": 0.7016883492469788,
                "sadness": 0.2189653068780899,
                "surprise": 0.00199463265016675
            }
        },
        {
            "autor": "luzmarina.nieto.94849",
            "emocion": "anger",
            "etiqueta": "NEG",
            "fecha": "2023-03-24T02:27:35.000Z",
            "id_comentario": "17993079022798756",
            "likes": 0,
            "original_texto": "desantishector todo el que se ha hecho rico empobreciendo al pueblo Colombiano es corrupto",
            "puntuacion": -0.9133086204528809,
            "res_analisis": {
                "NEG": 0.9133086204528809,
                "NEU": 0.06692910939455032,
                "POS": 0.019762301817536354
            },
            "res_emocion": {
                "anger": 0.7198909521102905,
                "disgust": 0.2547261118888855,
                "fear": 0.001876169117167592,
                "joy": 0.0038999097887426615,
                "others": 0.004716045688837767,
                "sadness": 0.014096331782639027,
                "surprise": 0.0007944991812109947
            }
        },
        {
            "autor": "alexespinosa8902",
            "emocion": "anger",
            "etiqueta": "NEG",
            "fecha": "2023-03-24T02:56:09.000Z",
            "id_comentario": "17969278199083987",
            "likes": 0,
            "original_texto": "Deje de ser amarillistas ",
            "puntuacion": -0.909913182258606,
            "res_analisis": {
                "NEG": 0.909913182258606,
                "NEU": 0.08171199262142181,
                "POS": 0.008374800905585289
            },
            "res_emocion": {
                "anger": 0.8543281555175781,
                "disgust": 0.090256467461586,
                "fear": 0.0026552563067525625,
                "joy": 0.0015641172649338841,
                "others": 0.04322679713368416,
                "sadness": 0.00671033002436161,
                "surprise": 0.0012588967802003026
            }
        },
        {
            "autor": "noris.palma",
            "emocion": "anger",
            "etiqueta": "NEU",
            "fecha": "2023-03-24T03:23:46.000Z",
            "id_comentario": "17971395929488243",
            "likes": 3,
            "original_texto": " ahí vamos y todas las reformas que pretende este nefasto gobierno no van a avanzar vamos con toda a hacer respetar nuestro país FUERAAAA el socialismo de Colombia ",
            "puntuacion": 0.45639586448669434,
            "res_analisis": {
                "NEG": 0.44364291429519653,
                "NEU": 0.45639586448669434,
                "POS": 0.09996119141578674
            },
            "res_emocion": {
                "anger": 0.9036192893981934,
                "disgust": 0.061203744262456894,
                "fear": 0.000894621480256319,
                "joy": 0.0034388829953968525,
                "others": 0.015139962546527386,
                "sadness": 0.01492689736187458,
                "surprise": 0.0007766803610138595
            }
        },
        {
            "autor": "yulisarteagahernandez",
            "emocion": "anger",
            "etiqueta": "NEG",
            "fecha": "2023-03-24T12:10:09.000Z",
            "id_comentario": "17961222356215996",
            "likes": 0,
            "original_texto": "Medios de pacotilla ",
            "puntuacion": -0.9022305607795715,
            "res_analisis": {
                "NEG": 0.9022305607795715,
                "NEU": 0.08969613909721375,
                "POS": 0.00807325541973114
            },
            "res_emocion": {
                "anger": 0.7796727418899536,
                "disgust": 0.1544232815504074,
                "fear": 0.0021222217474132776,
                "joy": 0.0023127642925828695,
                "others": 0.05354653298854828,
                "sadness": 0.006261928007006645,
                "surprise": 0.001660501933656633
            }
        },
        {
            "autor": "yulisarteagahernandez",
            "emocion": "others",
            "etiqueta": "NEU",
            "fecha": "2023-03-24T12:13:09.000Z",
            "id_comentario": "17851830437945883",
            "likes": 0,
            "original_texto": "norispalma te lo vas a tener que aguantar mínimo 3 años largos actualmente es el presidente de los Colombianos te guste o nooo",
            "puntuacion": 0.6190111041069031,
            "res_analisis": {
                "NEG": 0.3152884244918823,
                "NEU": 0.6190111041069031,
                "POS": 0.0657004788517952
            },
            "res_emocion": {
                "anger": 0.005096147768199444,
                "disgust": 0.001588159124366939,
                "fear": 0.00033078889828175306,
                "joy": 0.014318803325295448,
                "others": 0.9732552766799927,
                "sadness": 0.0037546493113040924,
                "surprise": 0.0016560365911573172
            }
        },
        {
            "autor": "piedadaogmail.co",
            "emocion": "anger",
            "etiqueta": "NEG",
            "fecha": "2023-03-24T12:32:35.000Z",
            "id_comentario": "18210135583239422",
            "likes": 1,
            "original_texto": "Que retiren las demás  Este gobierno es muy incoherente",
            "puntuacion": -0.9659240245819092,
            "res_analisis": {
                "NEG": 0.9659240245819092,
                "NEU": 0.02803664095699787,
                "POS": 0.0060393367893993855
            },
            "res_emocion": {
                "anger": 0.8644286394119263,
                "disgust": 0.11159099638462067,
                "fear": 0.0016054711304605007,
                "joy": 0.0007674156804569066,
                "others": 0.016466107219457626,
                "sadness": 0.004120818804949522,
                "surprise": 0.001020548166707158
            }
        },
        {
            "autor": "marthamorelo.s",
            "emocion": "others",
            "etiqueta": "NEU",
            "fecha": "2023-03-24T12:41:18.000Z",
            "id_comentario": "18353581687025038",
            "likes": 0,
            "original_texto": "sebastiangop9 el la manda a retirar  pero cuando ya no hay caso y en cierta forma se la hicieron retirar",
            "puntuacion": 0.732713520526886,
            "res_analisis": {
                "NEG": 0.2541542053222656,
                "NEU": 0.732713520526886,
                "POS": 0.013132219202816486
            },
            "res_emocion": {
                "anger": 0.0023598617408424616,
                "disgust": 0.001006809063255787,
                "fear": 0.000911669572815299,
                "joy": 0.0005840262747369707,
                "others": 0.9873257875442505,
                "sadness": 0.005583904683589935,
                "surprise": 0.002228054916486144
            }
        },
        {
            "autor": "25868rosa",
            "emocion": "others",
            "etiqueta": "POS",
            "fecha": "2023-03-24T16:44:10.000Z",
            "id_comentario": "18098971531314560",
            "likes": 0,
            "original_texto": "Dios dale claridad  a todo el equipo que apoya a nuestro presidente para que puedan hacer las cosas bien y puedan beneficiar a los más necesitados",
            "puntuacion": 0.8754416704177856,
            "res_analisis": {
                "NEG": 0.01930677518248558,
                "NEU": 0.10525158047676086,
                "POS": 0.8754416704177856
            },
            "res_emocion": {
                "anger": 0.0088938158005476,
                "disgust": 0.001774684526026249,
                "fear": 0.004514763597398996,
                "joy": 0.12257072329521179,
                "others": 0.8560807108879089,
                "sadness": 0.004956037271767855,
                "surprise": 0.0012094711419194937
            }
        },
        {
            "autor": "pastrana_luisa",
            "emocion": "others",
            "etiqueta": "POS",
            "fecha": "2023-03-24T22:57:19.000Z",
            "id_comentario": "18027404104490510",
            "likes": 0,
            "original_texto": "El es el que tiene q pedir q Dios le de claridad para hacer las cosas biendigo el presidente Petro",
            "puntuacion": 0.595402181148529,
            "res_analisis": {
                "NEG": 0.03422405943274498,
                "NEU": 0.3703737258911133,
                "POS": 0.595402181148529
            },
            "res_emocion": {
                "anger": 0.0022441584151238203,
                "disgust": 0.0007651638588868082,
                "fear": 0.001138989464379847,
                "joy": 0.0021673741284757853,
                "others": 0.9906533360481262,
                "sadness": 0.0020394730381667614,
                "surprise": 0.0009914463153108954
            }
        },
        {
            "autor": "betsyrussogonzalez",
            "emocion": "anger",
            "etiqueta": "NEG",
            "fecha": "2023-03-24T23:45:15.000Z",
            "id_comentario": "18178953334261133",
            "likes": 0,
            "original_texto": "Las reformas de hace 30 años si eran coherente viven es desinformando y tergiversando estos medios prepagos y amarrillista",
            "puntuacion": -0.9500204920768738,
            "res_analisis": {
                "NEG": 0.9500204920768738,
                "NEU": 0.04073307290673256,
                "POS": 0.009246411733329296
            },
            "res_emocion": {
                "anger": 0.8728156089782715,
                "disgust": 0.11602918803691864,
                "fear": 0.0015615118900313973,
                "joy": 0.0005772163858637214,
                "others": 0.004478382412344217,
                "sadness": 0.003981604706496,
                "surprise": 0.0005565708852373064
            }
        },
        {
            "autor": "juanguillermo09",
            "emocion": "others",
            "etiqueta": "NEG",
            "fecha": "2023-03-25T01:00:29.000Z",
            "id_comentario": "18019012810523487",
            "likes": 0,
            "original_texto": "Río desinformativo noticias gas ",
            "puntuacion": -0.7767739295959473,
            "res_analisis": {
                "NEG": 0.7767739295959473,
                "NEU": 0.20804594457149506,
                "POS": 0.01518003549426794
            },
            "res_emocion": {
                "anger": 0.2887393534183502,
                "disgust": 0.13635560870170593,
                "fear": 0.004795913118869066,
                "joy": 0.0021255763713270426,
                "others": 0.5455673933029175,
                "sadness": 0.01874588243663311,
                "surprise": 0.0036702521611005068
            }
        },
        {
            "autor": "rmartinezvergara",
            "emocion": "sadness",
            "etiqueta": "NEG",
            "fecha": "2023-03-25T13:39:12.000Z",
            "id_comentario": "17984529550945278",
            "likes": 0,
            "original_texto": "Después de estar perdidos la retiran que derrota tan bella le debe estar ardiendo todavía",
            "puntuacion": -0.9008901715278625,
            "res_analisis": {
                "NEG": 0.9008901715278625,
                "NEU": 0.08055894821882248,
                "POS": 0.018550902605056763
            },
            "res_emocion": {
                "anger": 0.006214448716491461,
                "disgust": 0.00793133769184351,
                "fear": 0.0049633183516561985,
                "joy": 0.016687018796801567,
                "others": 0.21463778614997864,
                "sadness": 0.7305603623390198,
                "surprise": 0.019005704671144485
            }
        },
        {
            "autor": "toscanoguillen",
            "emocion": "others",
            "etiqueta": "POS",
            "fecha": "2023-03-25T23:54:02.000Z",
            "id_comentario": "17949728465391061",
            "likes": 0,
            "original_texto": "dayrojsquitian así es",
            "puntuacion": 0.9492247700691223,
            "res_analisis": {
                "NEG": 0.006771874148398638,
                "NEU": 0.04400334879755974,
                "POS": 0.9492247700691223
            },
            "res_emocion": {
                "anger": 0.0008367157424800098,
                "disgust": 0.0005479474784806371,
                "fear": 0.00107562483754009,
                "joy": 0.2277543693780899,
                "others": 0.7626097202301025,
                "sadness": 0.001721997745335102,
                "surprise": 0.0054535651579499245
            }
        },
        {
            "autor": "noris.palma",
            "emocion": "sadness",
            "etiqueta": "NEG",
            "fecha": "2023-03-26T18:05:53.000Z",
            "id_comentario": "18047865292416966",
            "likes": 0,
            "original_texto": "yulisarteagahernandez pues no me gusta y si tengo que comerme el caramelo hasta el palito pero diferencia contigo es que no vote por eso ni creí en sus promesas como uds ques están llevando doble y eso duele más así que a mano ",
            "puntuacion": -0.956392228603363,
            "res_analisis": {
                "NEG": 0.956392228603363,
                "NEU": 0.038661617785692215,
                "POS": 0.004946134984493256
            },
            "res_emocion": {
                "anger": 0.15732307732105255,
                "disgust": 0.061453066766262054,
                "fear": 0.00184175546746701,
                "joy": 0.0042780544608831406,
                "others": 0.055740464478731155,
                "sadness": 0.7187579274177551,
                "surprise": 0.0006056673591956496
            }
        },
        {
            "autor": "yulisarteagahernandez",
            "emocion": "joy",
            "etiqueta": "POS",
            "fecha": "2023-03-26T19:17:11.000Z",
            "id_comentario": "17964671201168007",
            "likes": 0,
            "original_texto": "norispalma yo estoy viviendo sabroso mi voto no fue en vano  Muy satisfecha con el gobierno que tenemos",
            "puntuacion": 0.9573900103569031,
            "res_analisis": {
                "NEG": 0.004189285449683666,
                "NEU": 0.038420744240283966,
                "POS": 0.9573900103569031
            },
            "res_emocion": {
                "anger": 0.00032629998167976737,
                "disgust": 0.0006958909216336906,
                "fear": 0.0006338648381642997,
                "joy": 0.992889404296875,
                "others": 0.0022874707356095314,
                "sadness": 0.0009382784483022988,
                "surprise": 0.00222880975343287
            }
        },
        {
            "autor": "noris.palma",
            "emocion": "others",
            "etiqueta": "NEG",
            "fecha": "2023-03-27T01:06:03.000Z",
            "id_comentario": "17958217124297790",
            "likes": 0,
            "original_texto": "yulisarteagahernandez que pena bueno espera más sabrosura  chao he dicho!!!!!",
            "puntuacion": -0.6350826621055603,
            "res_analisis": {
                "NEG": 0.6350826621055603,
                "NEU": 0.32497090101242065,
                "POS": 0.03994645178318024
            },
            "res_emocion": {
                "anger": 0.002566410694271326,
                "disgust": 0.0030450590420514345,
                "fear": 0.0016534641617909074,
                "joy": 0.1361621767282486,
                "others": 0.6748121976852417,
                "sadness": 0.17101836204528809,
                "surprise": 0.010742312297224998
            }
        }
    ]
   
    response = client.post('/new-statistic', json={
        "owner": 'prueba',
        "name_post": "CpLNvujJ7PI",
        "data": data
    })
    print(response)
    assert response.status_code == 200
