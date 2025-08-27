
l = ["kaizen","binaya","pritish","manish"]

def remove(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n    



print(remove(l, "h"))
