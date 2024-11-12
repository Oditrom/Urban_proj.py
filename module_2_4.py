numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range (1,len(numbers)):
    flag = True   
    for j in range (2,numbers[i]):
        
        if numbers[i] % j ==0:
            flag = False
            
    if flag == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('Primes:',primes)  
print('Not primes:',not_primes)                   