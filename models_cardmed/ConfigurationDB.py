class ConfigurationDB:
    def __init__(self,id,company="",device="",model="",path="",lastupdate=""):
        self.id = id
        self.company = company
        self.device = device
        self.model = model
        self.path = path
        self.lastupdate = lastupdate

    def getJSON(self):
        data = {}
        data['id'] = self.id
        data['company'] = self.company
        data['device'] = self.device
        data['models'] = self.model
        data['path'] = self.path
        data['lastupdate'] = self.lastupdate
        return data
    def __str__(self):
        return str(self.getJSON())
        #return f"Configuration: {self.id} {self.company} {self.device} {self.models} {self.path} {self.lastupdate}"