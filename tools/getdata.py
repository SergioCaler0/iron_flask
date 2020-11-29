from config.configuration import db, collection

def mensaje_personaje(nombre):
    """
    Hacemos una query a la base de datos para sacar las frases de un personaje
    """
    query = {"character_name":f"{nombre}"}
    frases = list(collection.find(query, {"_id":0}))
    return frases