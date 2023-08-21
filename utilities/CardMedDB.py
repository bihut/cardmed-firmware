import json
import os
import time

import bson
import pymongo
from dotenv import load_dotenv
from pymongo import MongoClient

class CardMedDB:
    def __init__(self) -> None:
        super().__init__()
        script_path = os.path.abspath(__file__)  # i.e. /path/to/dir/foobar.py
        script_dir = os.path.split(script_path)[0]
        script_dir = os.path.split(script_dir)[0]
        rel_path = "configuration/database.json"
        abs_file_path = os.path.join(script_dir, rel_path)
        f = open(abs_file_path)
        data = json.load(f)
        url = "mongodb://"+str(data['username'])+":"+str(data['password'])+"@"+str(data['url'])+":"+str(data['port'])+"/?authMechanism=DEFAULT"
        aux = MongoClient(url)
        self.db = aux.cardmed
    def insertNewData(self,values,configuration):
        data = {}
        data['timestamp'] = int(time.time())
        data['configuration'] = str(configuration)
        try:
            if type(values) is not dict:
                js = json.loads(values)
                data['values'] = js
            else:
                data['values']=values
            res = self.db.cardmed_data.insert_one(data)
            return self.get_by_id(res.inserted_id)
        except:
            pass
        return None

    def insertNewConfiguration(self,configuration):
        try:
            jsonconf = configuration
            if type(configuration) is not dict:
                jsonconf = json.loads(configuration)

            res = self.db.cardmed_configuration.insert_one(jsonconf)
            return self.get_by_id(res.inserted_id)
        except:
            pass
        return None

    def getConfigurationByID(self, configurationid):
        data = self.db.cardmed_configuration.find({"id": bson.ObjectId(configurationid)})
        return [{**session, "_id": str(session["_id"])} for session in data]

    def getConfigurationByModelCompany(self, model,company):
        data = self.db.cardmed_configuration.find({"model": str(model),"company":str(company)})
        return [{**session, "_id": str(session["_id"])} for session in data]

    def getDataByTime(self,starttime,endtime,configuration):
        data = self.db.cardmed_data.find({"configuration": str(configuration), "timestamp":
            {'$gte': int(starttime),
             '$lte': int(endtime)}
                                    })
        return [{**session, "_id": str(session["_id"])} for session in data]


    def insertUpdateSettings(self,samplerate=60,uploaddata=False):
        pass