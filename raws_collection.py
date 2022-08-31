from urllib.request import urlopen
import json
import pandas as pd
import time
from datetime import datetime, timedelta

# raws_collection is a file that grabs the latest RAWS location data every 24 hours
# This is done by creating a continuous while loop that initially grabs the latest data
# Then sets a dt variable to 24 hours ahead. There is a nested while loop that then runs until 
# The current time equals the dt variable. The nested loop then ends and we loop back through the 
# outerloop restarting the process of grabing data, setting time ahead and waiting for the nested 
# loop
while 1:
    try:
        with urlopen('https://api.synopticdata.com/v2/stations/latest?&token=6f15765b51fa4a69b6787cc3693da767&within=60&units=english&country=us&network=2') as response:
            stations = json.load(response)
        df= pd.json_normalize(stations['STATION'])
        df_raws = pd.DataFrame().assign(Name=df['NAME'], Longitude=df['LONGITUDE'], Latitude=df['LATITUDE'], Temperature=df['OBSERVATIONS.air_temp_value_1.value'], Dew_Point_Temp=df['OBSERVATIONS.dew_point_temperature_value_1d.value'], Relative_Humidity=df['OBSERVATIONS.relative_humidity_value_1.value'], Wind_Speed=df['OBSERVATIONS.wind_speed_value_1.value'], Wind_Gust=df['OBSERVATIONS.wind_gust_value_1.value'], Pressure=df['OBSERVATIONS.pressure_value_1d.value'], Heat_Index=df['OBSERVATIONS.heat_index_value_1d.value'], Fuel_Temp=df['OBSERVATIONS.fuel_temp_value_1.value'], Fuel_Moisture=df['OBSERVATIONS.fuel_moisture_value_1.value'])
        df_raws['Longitude']= df_raws['Longitude'].astype(float, errors = 'raise')
        df_raws['Latitude']= df_raws['Latitude'].astype(float, errors = 'raise')
        df_raws.to_feather('./raws.ftr')
        print("success")
    except:
        print("Couldn't grab live data at "+ str(datetime.now()))

    dt = datetime.now() + timedelta(minutes=30)
    
    while datetime.now() < dt:
        time.sleep(1)