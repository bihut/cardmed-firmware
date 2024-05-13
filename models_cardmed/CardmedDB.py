from utils import Utils


class CardmedDB:
    def __init__(self,deviceid,customid=Utils.Utils.getUUID(),address="",country="es",entity="",owner="",owneremail="",ownerphone="",deployed=Utils.Utils.getCurrentTimeStamp()):
        self.deviceid = deviceid
        self.customid = customid
        self.address = address
        self.country = country
        self.entity = entity
        self.owner = owner
        self.owneremail = owneremail
        self.ownerphone = ownerphone
        self.deployed = deployed

    def getJSON(self):
        data = {}
        data['deviceid'] = self.deviceid
        data['customid'] = self.customid
        data['address'] = self.address
        data['country'] = self.country
        data['entity'] = self.entity
        data['owner'] = self.owner
        data['owneremail'] = self.owneremail
        data['ownerphone'] = self.ownerphone
        data['deployed'] = self.deployed

        return data
    def __str__(self):
        return str(self.getJSON())
        #return f"Configuration: {self.id} {self.company} {self.device} {self.models} {self.path} {self.lastupdate}"