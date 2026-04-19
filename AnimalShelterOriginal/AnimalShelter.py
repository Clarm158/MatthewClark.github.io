from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self):
        # Initializing the MongoClient. This helps to
        # access the MongoDB database and collections. 
        # This is hard-wired to use the aac database, the
        # animals collection, and the aac user.
        # Definitions of the connection string variables are 
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect 
        # your own instance of MongoDB!
        # 
        # Connection Variables
        # 
        USER = 'aacuser'
        PASS = 'snhu123'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34667
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            result = self.database.animals.insert_one(data) # data should be dictionary
            if result.acknowledged:
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# Create method to implement the R in CRUD
    def read(self, query):
        if query is not None:
            result = self.database.animals.find(query)
            return list(result) # Return as a list of documents
        else:
            raise Exception("Nothing to read, because query parameter is empty")
            
# Create method to implement the U in CRUD
    def update(self, query, new_values):
        if query and new_values:
            result = self.database.animals.update_many(query, {"$set": new_values})
            return result.modified_count
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            
# Create method to implement the D in CRUD
    def delete(self, query):
        if query:
            result = self.database.animals.delete_many(query)
            return result.deleted_count
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            