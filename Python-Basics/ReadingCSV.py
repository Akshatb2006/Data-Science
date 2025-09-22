# To read CSV files through pandas, we use pd.read_csv() method
from google.colab import files
import pandas as pd

uploaded = files.upload()

# df = pd.read_csv('people_data.csv')
# print("\n\nFirst n rows\n:",df.head())

lf = pd.read_csv('netflix.csv')
print("\n\nFirst n rows\n:",lf.head())