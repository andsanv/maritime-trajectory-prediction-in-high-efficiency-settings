import pandas as pd
import matplotlib.pyplot as plt
import os
import glob


data_folder = "/Users/dani/Desktop/AIS_DL_project/Data/AIS_dclean_11_03.parquet"


# Using pyarrow (default if installed)
df = pd.read_parquet("/Users/dani/Desktop/AIS_DL_project/Data/AIS_dclean_11_03.parquet/MMSI=210174000")

df['Timestamp'] = pd.to_datetime(df['Timestamp'])

df = df.set_index('Timestamp')

df_5min = df.resample('5T').mean(numeric_only=True)

#miising time stamps are filled using interpolation with the maximum gap of 4
#df_5min = df_5min.interpolate(limit=4, limit_direction='both')
#drop rows that still have NaN values after interpolation
#df_5min = df_5min.dropna()

df_5min = df_5min.reset_index()  # brings Timestamp back as a column
df = df.reset_index()


#with open('data.txt', 'w') as f:
#    f.write(df_5min.to_string(index=False))

#with open('data_raw.txt','w') as f:
#    f.write(df.to_string(index=False))

# Check the first few rows
#print(df.head(len(df)))
#print(pd.set_option('display.max_rows', None) or df)

import matplotlib.pyplot as plt

plt.plot(df['Timestamp'], df['Latitude'], label='Latitude')
plt.plot(df['Timestamp'], df['Longitude'], label='Longitude')
plt.legend()
plt.show()
