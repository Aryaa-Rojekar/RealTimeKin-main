import numpy as np
import pandas as pd

csv_file_path = 'sit_walk.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path)
numpy_array = df.values
npy_file_path = 'sit_walk.npy'  # Replace with your desired output path
np.save(npy_file_path, numpy_array)