
def greatest(a,b,c):
    if(a >b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

a = 5
b = 6
c = 1
 
print(greatest(a,b,c))