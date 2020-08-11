import pyowm
import config
import json
from core.weather import flag_emoji

owm = config.owm

def coord(s):
    obs = owm.weather_at_place(s)
    l = obs.get_location()
    lon = l.get_lon()
    lat = l.get_lat()
    t = s.split(',')[1]
    n = t.lstrip(' ')
    m = flag_emoji(n)
    if lat > 0:
        s1 = " N "
    else:
        s1 = " S "
    if lon > 0:
        s2 = " E "
    else:
        s2 = " W "
    return m + s.split(',')[0] + ' coordinates: ' + str(abs(lat)) + '°' + s1 + str(abs(lon)) + '°' + s2

def output(s):
    if len(s.split(',')) > 2:
        return 'Enter the name of the city as in the example!'
    n = ' '
    for i in range(len(s)):
        if s[i] == ',':
            p = s.split(',')[1]
            n = p.lstrip(' ')
            break
    if n != ' ':   
        data1 = 'data/countries.json'
        with open(data1, 'r') as f1:
            db1 = json.load(f1)
            for i in db1: 
                if n == i['name']:
                    p = i['sortname']
    else:
        return 'Enter the name of the city as in the example!'
    data2 = 'data/citylist.json'
    with open(data2, 'r') as f2:
        db2 = json.load(f2)
        for i in db2:
            m = s.split(',')[0]
            if  (m == i['name'] and p == i['country']):            
                return coord(m + ', ' + p)
        return 'Enter the name of the city as in the example!'