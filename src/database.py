import pymongo


class database(object):
    database=None

    @staticmethod
    def init(username,password):
        uri="mongodb+srv://"+username+":"+password+"@cluster0-kw0te.mongodb.net/test?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri)
        database.database = client['games']

    @staticmethod
    def getOne(col,one=None):
        element=database.database[col].find_one(one)
        return element

    @staticmethod
    def getMany(col,filter=None):
        element=database.database[col].find(filter)
        return element

    @staticmethod
    def insertOne(col,object):
        element=database.database[col].insert_one(object)
        return {"id":element.inserted_id,"object":object}


