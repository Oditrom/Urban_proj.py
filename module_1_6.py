my_dict = {'Иван': 1900, "Диван": 1910, "Ипполит": 1920, "Замполит": 1937}
print("Dict:",my_dict)
print('Existing value:',my_dict['Иван'])
print('Not existing value:',my_dict.get('Не_Иван'))
my_dict_2 ={'Маша':1930,'Саша':1940}
my_dict.update(my_dict_2)
print('Deleted value:',my_dict.pop('Маша'))
print('Modified dictionary:',my_dict)

my_set ={1,2,3,9,4,5,6,5,4,3,5,6,7,}
print('Set:',my_set)
my_set.add(0)
my_set.add('#')
my_set.discard(3)
print('Modified set:',my_set)
