from urllib.request import urlopen
import json
import pandas as pd
import time
from datetime import datetime, timedelta


while 1:
    try:
        with urlopen('https://api.synopticdata.com/v2/stations/metadata?&token=6f15765b51fa4a69b6787cc3693da767&network=2&country=us&status=active') as response:
            stations = json.load(response)
        df= pd.json_normalize(stations['STATION'])
        df_raws = pd.DataFrame().assign(Name=df['NAME'], Longitude=df['LONGITUDE'], Latitude=df['LATITUDE'])
        df_raws['Longitude']= df_raws['Longitude'].astype(float, errors = 'raise')
        df_raws['Latitude']= df_raws['Latitude'].astype(float, errors = 'raise')
        df_raws.to_feather('./raws.ftr')
        print("success")
    except:
        print("Couldn't grab live data at "+ str(datetime.now()))

    dt = datetime.now() + timedelta(hours=24)
    dt = dt.replace(minute=00)
    
    while datetime.now() < dt:
        time.sleep(1)