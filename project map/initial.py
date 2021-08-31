from geocoder import ip
from googleplaces import GooglePlaces,types,lang
from requests import get
def myloc():
    loc=ip('me')
    #for a in loc.json:
        #print(a, loc.json[a])
    return {'lat':loc.latlng[0],'lng':loc.latlng[1]}
'''def myloc2():
    ip='10.12.136.238'
    r=get('http://freegeoip.net/json/'+ip).json()
    for a in r:
        print(a,r[a])
    return {'lat':r['latitude'],'lng':r['longitude']}'''
def result():
    gsearch=GooglePlaces('AIzaSyATL_kVBEI0KiaMF4wm4gjciGWaWk6JjcI')
    latlng=myloc()
    print(latlng)
    query=gsearch.nearby_search(lat_lng=latlng,radius=10000,types=[types.TYPE_HOSPITAL])
    print(query)
    for a in query.raw_response["results"]:
        print(a['name'])
        print(a['geometry']['location']['lat'],a['geometry']['location']['lng'])
if __name__=="__main__":
    result()
    #loc()                            
    
