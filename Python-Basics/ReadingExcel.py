# To read an excel file, we make use of the pd.read_excel() method
from google.colab import files
import pandas as pd

uploaded = files.upload()

df = pd.read_excel('Youth_Brand_SWOT_Master.xlsx')
print("\n\nFirst n rows\n:",df.head())