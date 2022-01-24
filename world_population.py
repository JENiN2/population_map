import json

# Список заполняется данными.
filename = "data/population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

print('World population in 2010:\n')
# Вывод населения за 2010 год.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        value = pop_dict['Value']
        print(country_name + ': ' + value)
