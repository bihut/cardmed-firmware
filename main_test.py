from Services.Services import Services

'''
card = CardMedDB()
values={}
values["hr"]=54
values["sp"]=100

#card.insertNewData(values,configuration="asd9asd9090d")
res=card.getDataByTime(starttime=1692608000,endtime=1692609999,configuration="asd9asd9090d")
print(res)
'''

#res,state=Services.connectWifi("Redmi Note 8","7988555e218b")
#print("res",res)
#print("state",state)
Services.generateQRCode("probando textooooo","qrcode.png")