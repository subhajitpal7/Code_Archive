import googlemaps
from datetime import datetime
from json import dump
from readAPI import readAPI
def ini():
    global gmaps
    api=readAPI()
    gmaps=googlemaps.Client(key=api)
def getroutes(source,dest):
    global gmaps
    f=open('data'+source+dest+'.txt','w',encoding='utf-8')
    r=directions_result = gmaps.directions(source,
                                     dest,
                                     mode="transit",
                                     departure_time=datetime.now())
    dump(r,f,indent=4,sort_keys=True,ensure_ascii=False)
    return r
if __name__=="__main__":
    #gmaps=0
    ini()
    source,dest=map(str,input().split())
    print(getroutes(source,dest))
