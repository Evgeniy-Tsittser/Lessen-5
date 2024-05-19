# Работа со списком
my_list = ['pen','pencil','ruler','copybook','book']
print(my_list)
print(my_list[0:5:4])
print(my_list[2:5:1])
my_list[2] = 'compass'
print(my_list)
# Работа со словарем
my_dict = {'pen':'ручка','pencil':'карандаш','ruler':'линейка','copybook':'тетрадь','book':'книга'}
print(my_dict)
print(my_dict['ruler'])
my_dict['copybook'] = 'блокнот'
print(my_dict)
my_dict.update({'glass':'стакан'})
print(my_dict)