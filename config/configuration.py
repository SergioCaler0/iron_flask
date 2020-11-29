
import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

DBURL = os.getenv("URL")

# VAMOS A CONECTAR CON LA BASE DE DATOS DE MONGO EN LOCAL
if not (DBURL):
    raise ValueError("Tienes que especificar una URL please")


client = MongoClient(DBURL)
db =client.get_database()
collection = db["frases"]

