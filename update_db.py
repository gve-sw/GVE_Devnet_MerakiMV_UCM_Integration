from env_var import Database, Cluster, Collection
from pymongo import MongoClient
from datetime import datetime


#Inserts the details into the Database for recording purposes
def database_update(vehicle):
    date = datetime.now()
    today = date.strftime('%H:%M %m-%d-%Y')
    cluster = MongoClient(Database)
    db = cluster[Cluster]
    collection = db[Collection]
    collection.insert_one({'vehicle': vehicle, 'date': today})