import data_processing as dp
csv_read = dp.ReadCSV('movies').fetch
table = dp.Table('movies', csv_read)

table2 = table.filter(lambda x: x['Genre'] == 'Comedy').aggregate(lambda y: sum(y)/len(y), 'Worldwide Gross')
print('Average Worldwide gross for comedy movies is ' + str(table2))
table3 = table.filter(lambda x: x['Genre'] == 'Drama').aggregate(lambda y: min(y), 'Audience score %')
print(f'Minimum ‘Audience score %’ for ‘Drama’ movies is {table3}')
