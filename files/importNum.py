import numpy as np

data = "Lending-Company-Numeric-Data-NAN.csv"

load_data = np.genfromtxt(data, delimiter=";")
print(load_data)