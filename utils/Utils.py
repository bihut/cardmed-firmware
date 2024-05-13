import os

from utils import CardmedConstants


class Utils:
    @staticmethod
    def checkIfCardmedDevice():
        import os
        myhost = os.uname()[1]
        if "raspberrypi" in myhost.lower() or "carmed" in myhost.lower():
            return True

        return False
    @staticmethod
    def getUUID():
        import uuid

        myuuid = uuid.uuid4()
        return str(myuuid)

    @staticmethod
    def getCurrentTimeStamp():
        import time

        # ts stores the time in seconds
        ts = time.time()
        return ts
    @staticmethod
    def createCardmedStructure(cardmedid=None):
        if not os.path.exists(CardmedConstants.CardmedConstants.CARDMED_ROOTPATH):
            # Si no existe, crearlo
            try:
                os.makedirs(CardmedConstants.CardmedConstants.CARDMED_ROOTPATH)
            except OSError as e:
                pass
        if not os.path.exists(CardmedConstants.CardmedConstants.CARDMED_DB_PATH):
            # Si no existe, crearlo
            try:
                os.makedirs(CardmedConstants.CardmedConstants.CARDMED_DB_PATH)
            except OSError as e:
                pass

        if not os.path.exists(CardmedConstants.CardmedConstants.CARDMED_DEVICES_CONFIG_PATH):
            # Si no existe, crearlo
            try:
                os.makedirs(CardmedConstants.CardmedConstants.CARDMED_DEVICES_CONFIG_PATH)
            except OSError as e:
                pass