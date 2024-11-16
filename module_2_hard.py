n = int(input())
a  = ""
for i in range (1,n):
    for j in range(i,n):
        if n % (i + j) == 0 and i !=j:
            a += str(i)
            a += str(j)
print(n,"-",a)            
