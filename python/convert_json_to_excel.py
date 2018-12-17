import json
import csv
import pandas as pd
from pandas.io.json import json_normalize

for i in range(number):
 data = pd.read_json("excel" + str(i)+ ".json")
 df = json_normalize(data["value"])
 df.to_csv("excel" + str(i) + ".csv")