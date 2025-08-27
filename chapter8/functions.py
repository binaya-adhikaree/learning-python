
#  functions in python
def average():
    a = int(input("enter your number: "))
    b = int(input("enter your number: "))
    c = int(input("enter your number: "))

    avg = (a + b + c)/3
    print(f"your average is: {avg}")

average() 


# function with args and return value
def greet(name):
    print("hello " + name)
    return "Thanks for visiting"


a =  greet("kaizen")
print(a)


# default arguments

def func(name, ending = "thank you"):
    print(f"hello {name}")
    print(ending)


func("kaizen")



