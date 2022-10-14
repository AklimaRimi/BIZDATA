import pandas as pd

data = pd.read_csv('BIZDATA_BackEnd_TestData.csv')
print(data.head())
print(data.shape)
print(data.columns)
print(data.dtypes)

# data = data[['Date','gross income']]

# print(data.head())

# data['Date'] = pd.to_datetime(data['Date'])
# print(data.head())

# data = data.sort_values('Date').reset_index()
# data.index = data['Date']
# print(data.head())

# print(data.resample('M').max())

