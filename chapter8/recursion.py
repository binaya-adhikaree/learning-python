
def factiorial(n):
    if(n == 0 or n == 1):
        return 1
    return n *  factiorial(n-1)    

n = int(input("enter your number: "))
print(f"The factorial of {n} is {factiorial(n)}")