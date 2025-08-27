 

 f = open("./text.txt")

 data = f.read()
 if("hi" in data):
    print("the word is present in the data")
 else:
    print("the word is not present in the data  ")   
 print(data)