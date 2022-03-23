import pandas as pd

census = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
value_count = census['Primary Fur Color'].value_counts()
data = value_count.to_frame().reset_index()

# pd.Series(value_count).to_csv('result.csv')
data.columns = ['Primary Fur Color', 'Count']
pd.DataFrame(data).to_csv('results.csv')

# value_count.rename('Primary Fur Color')
# print(pd.DataFrame(value_count, columns=['Primary Fur Color', 'Counts']))
