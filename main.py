from opensky_api import OpenSkyApi 
import pandas as pd

api = OpenSkyApi() 
states = api.get_states()
flights_data =[["longitude", "latitude", "baro_altitude","velocity"]]
for s in states.states:
    print("(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))
    flights_data.append([s.longitude, s.latitude, s.baro_altitude, s.velocity])

df =pd.DataFrame(flights_data)

df.to_csv("data.csv",index=False)