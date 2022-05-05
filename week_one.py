#
# Pandas import edilmeli
# Dosyamızın adresi belirlenmeli
# DataFrame objesi oluşturulmalı
# 
#

import pandas as pd

url = "addresses.csv"

df = pd.read_csv(url,header=None)

header = ["a","b","c","d","e","f"]

df.columns = header

export = "test.json"

df.to_json(export)

print(df.head(1)) #Gets only first row

print(df.describe()) # Prints general information about table

print(df.dtypes) # Returns table coulmn types as pandas values