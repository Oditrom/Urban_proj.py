a, b, c = int(input()), int(input()), int(input())
if a == b and b == c and c == a:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)  
