
class Utils:
    @staticmethod
    def checkIfCardmedDevice():
        import os
        myhost = os.uname()[1]
        if "raspberrypi" in myhost.lower() or "carmed" in myhost.lower():
            return True

        return False