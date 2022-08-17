from urllib.request import urlopen
import json
import pandas as pd
import plotly.express as px


with urlopen('https://api.synopticdata.com/v2/stations/metadata?&token=6f15765b51fa4a69b6787cc3693da767&network=2&country=us&status=active') as response:
    stations = json.load(response)
df= pd.json_normalize(stations['STATION'])
df_raws = pd.DataFrame().assign(Name=df['NAME'], Longitude=df['LONGITUDE'], Latitude=df['LATITUDE'])
df_raws['Longitude']= df_raws['Longitude'].astype(float, errors = 'raise')
df_raws['Latitude']= df_raws['Latitude'].astype(float, errors = 'raise')
df_raws.to_feather('./raws.ftr')

fig_raws = px.scatter_mapbox(df_raws, lat="Latitude", lon="Longitude", hover_name="Name", hover_data=["Name"], zoom=3, height=300)
fig_raws.update_layout(
    mapbox_style="white-bg",
    mapbox_layers=[
        {
            "below": 'traces',
            "sourcetype": "raster",
            "sourceattribution": "United States Geological Survey",
            "source": [
                "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"
            ]
        }
    ])
fig_raws.update_layout(
autosize=False,
margin = dict(
        l=0,
        r=0,
        b=0,
        t=0,
        pad=4,
        autoexpand=True
    ),
    height=800,
)
fig_raws.show()
