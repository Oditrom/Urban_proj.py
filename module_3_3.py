def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params() 
   
print_params(b = 25) 

print_params(c = [1,2,3])

values_list =[True, 0, '0']
values_dict = {'a' : 9, 'b' : '9', 'c' : False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [None, True]
print_params(*values_list_2,42)