import numpy as np
import pandas as pd

csv_file_path = 'C:/Users/laure\Box/Lauren-Projects/NML/Code/RealTimeKin/RealTimeKin-main/recordings/demo/boxing.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path)
numpy_array = df.values
npy_file_path = 'C:/Users/laure\Box/Lauren-Projects/NML/Code/RealTimeKin/RealTimeKin-main/recordings/demo/boxing.npy'  # Replace with your desired output path
np.save(npy_file_path, numpy_array)