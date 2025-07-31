import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import plotly.express as px

#data = pd.read_csv('C:/Users/aryaa/Desktop/research/base_code/RealTimeKin-main/recordings/demo/sit_walk.csv')
#fig = px.line(data, x = range(0, len(data)), y = 'AccelX_1', title = 'Simulation')
data = np.load('C:/Users/aryaa/Desktop/research/base_code/RealTimeKin-main/recordings/demo/raw_imu_0.npy')

#accel_col = [col for col in data.columns if "Accel" in col]
#gyro_col = [col for col in data.columns if "Gyro" in col]
#fig.show()
plt.figure() 
#plt.plot(range(10000),data[gyro_col].iloc[0:10000].values)
plt.plot(range(len(data)),data)
plt.show()


