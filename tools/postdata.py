from config.configuration import db, collection

def insertamensaje(escena,personaje,frase):
    """
    funcion que inserta los datos en mongo es el momento de 
    revisar que todos los datos esten comom queramos.
    """

    dict_insert = { "scene" : f"{escena}",
    "character_name" : f"{personaje}",
    "dialogue" : f"{frase}",   
    }
    collection.insert_one(dict_insert)
