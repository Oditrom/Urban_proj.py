def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0]) 
    if len(str(number)) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if number == 0:
        return 1
    else:
        return first    
    


