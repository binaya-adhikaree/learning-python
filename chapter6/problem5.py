list = [
    "Kaizen",
    "Yamato",
    "Luffy",
    "Zoro",
    "Nami"
]


name = input("enter your name")

if(name in list):
    print(f"{name} exists in the list", )
else:
    print(f"{name} dont exists on the list")