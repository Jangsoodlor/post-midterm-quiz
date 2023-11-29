import data_processing as dp
csv_read = dp.ReadCSV('movies').fetch
table = dp.Table('movies', csv_read)
database = dp.DB()
database.insert(table)


table2 = table.filter(lambda x: x['Genre'] == 'Comedy').aggregate(lambda y: sum(y)/len(y), 'Worldwide Gross')
print('Average Worldwide gross for comedy movies is ' + str(table2))
table3 = table.filter(lambda x: x['Genre'] == 'Drama').aggregate(lambda y: min(y), 'Audience score %')
print(f'Minimum ‘Audience score %’ for ‘Drama’ movies is {table3}')
table4 = table.filter(lambda x: x['Genre'] == 'Fantasy').aggregate(lambda y: len(y), 'Film')
print(f'The number of fantasy movie is {table4}')

dict = {}
dict['Film'] = 'The Shape of Water'
dict['Genre'] = 'Fantasy'
dict['Lead Studio'] = 'Fox'
dict['Audience score %'] = '72'
dict['Profitability'] = '9.765'
dict['Rotten Tomatoes %'] = '92'
dict['Worldwide Gross'] = '195.3'
dict['Year'] = '2017'

table.insert_row(dict)
table5 = table.filter(lambda x: x['Genre'] == 'Fantasy').aggregate(lambda y: len(y), 'Film')
print(f'The number of fantasy movie after updating is {table5}')

table6 = table.update_row('Film', 'A Serious Man', 'Year', 2022).filter(lambda x: x['Film'] == 'A Serious Man')
print(table6)