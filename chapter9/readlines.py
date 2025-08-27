


f = open('./newfile.txt')
# line1 = f.readline()
# print(line1)

# line1 = f.readline()
# print(line1) 
# line3 = f.readline()
# print(line3)
- 

line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()  


with open("./newfile.txt") as f
print(f.read())
