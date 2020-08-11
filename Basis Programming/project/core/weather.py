import pyowm
import json
import config
from core.emoji import *

owm = config.owm

def temp(s):
    obs = owm.weather_at_place(s)
    w = obs.get_weather()
    t = s.split(',')[1]
    n = t.lstrip(' ')
    m = flag_emoji(n)
    if w.get_wind()['speed'] > 9:
        table = "Weather in " + s.split(',')[0] + m + " now\t" + str(emoji(w.get_status())) + storm + "\n"
    else:
        table = "Weather in " + s.split(',')[0] + m + " now\t" + str(emoji(w.get_status())) + "\n"
    temp = term + "Air temperature: " + str(round(w.get_temperature('celsius')['temp'])) + "°C\n"
    if w.get_wind()['speed'] == 0:
        wind = 'There is no wind!'
    else:
        wind = winde + deg(s) + " wind at a speed of " + str(w.get_wind()['speed']) + " m/s\n"
    humidity = hum + "Air humidity: " + str(w.get_humidity()) + "%\n"
    return table + temp + wind + humidity

def flag_emoji(s):
    data = 'data/flagemoji.json'
    f = ' '
    with open(data, 'r') as g:
        db = json.load(g)
        for i in db:
            if s == i["code"]:
                f = i["emoji"]
    return f

def deg(s):
    obs = owm.weather_at_place(s)
    w = obs.get_weather()
    if (w.get_wind()['deg'] >= 0 and w.get_wind()['deg'] <= 22.5 or w.get_wind()['deg'] > 337.5 and w.get_wind()['deg'] <= 360):
        return 'North'
    if (w.get_wind()['deg'] > 22.5 and w.get_wind()['deg'] <= 67.5):
        return 'North-east'
    if (w.get_wind()['deg'] > 67.5 and w.get_wind()['deg'] <= 112.5):
        return 'East'
    if (w.get_wind()['deg'] > 112.5 and w.get_wind()['deg'] <= 157.5 ):
        return 'South-east'
    if (w.get_wind()['deg'] > 157.5 and w.get_wind()['deg'] <= 202.5 ):
        return 'South'
    if (w.get_wind()['deg'] > 202.5 and w.get_wind()['deg'] <= 247.5 ):
        return 'South-west'
    if (w.get_wind()['deg'] > 247.5 and w.get_wind()['deg'] <= 292.5):
        return 'West'
    if (w.get_wind()['deg'] > 292.5 and w.get_wind()['deg'] <= 337.5):
        return 'North-west'

def emoji(t):
    if t:
        if str(t) == 'Rain':
            return rain
        elif str(t) == 'Snow':
            return snowflake + ' ' + snowman
        elif str(t) == 'Haze' or str(t) == 'Mist':
            return atmosphere
        elif str(t) == 'Clear':
            return clear
        elif str(t) == 'Clouds':
            return clouds
        else:
            return default
    else:
        return default

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
        return 'Enter the name of the city as in the example!!'
    data2 = 'data/citylist.json'
    with open(data2, 'r') as f2:
        db2 = json.load(f2)
        for i in db2:
            m = s.split(',')[0]
            if  (m == i['name'] and p == i['country']):
                return temp(m + ', ' + p)
        return 'Enter the name of the city as in the example!'