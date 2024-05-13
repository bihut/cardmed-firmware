from utils.Utils import Utils


class MonitorDataDB:
    def __init__(self,created=Utils.getCurrentTimeStamp(),configuration_id=-1,att="",val=-1):
        self.created = created
        self.configuration_id = configuration_id
        self.att = att
        self.val = val

    def getJSON(self):
        data = {}
        data['created'] = self.created
        data['configuration_id'] = self.configuration_id
        data['att'] = self.att
        data['val'] = self.val

        return data
    def __str__(self):
        return str(self.getJSON())
        #return f"Configuration: {self.id} {self.company} {self.device} {self.models} {self.path} {self.lastupdate}"