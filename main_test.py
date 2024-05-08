from services.services import Services
from utilities.CardMedDB import CardMedDB
'''
card = CardMedDB()
values={}
values["hr"]=54
values["sp"]=100

#card.insertNewData(values,configuration="asd9asd9090d")
res=card.getDataByTime(starttime=1692608000,endtime=1692609999,configuration="asd9asd9090d")
print(res)
'''

lista=Services.connectedNetwork()
print(lista)