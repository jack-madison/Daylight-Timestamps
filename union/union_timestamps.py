import pandas as pd
import numpy as np
import datetime
from astral.sun import sun
from astral import LocationInfo

df = pd.read_csv('./union/union_panel.csv')

df["dawn"] = np.nan
df["sunrise"] = np.nan
df["sunset"] = np.nan
df["dusk"] = np.nan

for x in range(len(df)):
    location = LocationInfo(name = 'Japan', region = 'Japan', timezone = 'Japan', latitude = df['mun_Y'][x], longitude = df['mun_X'][x])
    s = sun(location.observer, date=datetime.date(df['year'][x], df['month'][x], df['day'][x]), tzinfo = "Japan")
    df["dawn"][x] = s["dawn"]
    df["sunrise"][x] = s["sunrise"]
    df["sunset"][x] = s["sunset"]
    df["dusk"][x] = s["dusk"]
    x

df['dawn'] = pd.to_datetime(df['dawn'])
df['dawn_h'] = df['dawn'].dt.hour
df['dawn_m'] = df['dawn'].dt.minute
df['dawn_s'] = df['dawn'].dt.second

df['sunrise'] = pd.to_datetime(df['sunrise'])
df['sunrise_h'] = df['sunrise'].dt.hour
df['sunrise_m'] = df['sunrise'].dt.minute
df['sunrise_s'] = df['sunrise'].dt.second

df['sunset'] = pd.to_datetime(df['sunset'])
df['sunset_h'] = df['sunset'].dt.hour
df['sunset_m'] = df['sunset'].dt.minute
df['sunset_s'] = df['sunset'].dt.second

df['dusk'] = pd.to_datetime(df['dusk'])
df['dusk_h'] = df['dusk'].dt.hour
df['dusk_m'] = df['dusk'].dt.minute
df['dusk_s'] = df['dusk'].dt.second

df = df.drop(columns = ['dawn', 'sunrise', 'sunset', 'dusk'])

df.to_csv('./union/union_panel_timestamped.csv', index = False)