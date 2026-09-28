import pandas as pd

data = "Lending-company.json"
data_load = pd.read_json(data)
print(data_load)