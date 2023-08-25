from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'CardMed Device Working'

@app.route("/wifi",methods=["POST"])
def setWifiConnection():
	pass

@app.route("/configuration",methods=["POST"])
def setConfiguration():
	pass
@app.route("/configuration",methods=["GET"])
def getCurrentConfiguration():
	pass

@app.route("/configuration/all",methods=["GET"])
def getAllConfigurations():
	pass


@app.route("/data/<starttime>/<endtime>",methods=["GET"])
def getData(starttime,endtime):
	pass

@app.route("/data/realtime",methods=["GET"])
def getDataRealTime():
	pass

# main driver function
if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5555,debug=False)
