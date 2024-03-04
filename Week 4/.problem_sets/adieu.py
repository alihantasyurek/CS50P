name = []

while True:
    try:
        name += [input("Name: ")]
    except EOFError:
        break

length = len(name) - 1

name[0] = "to " + name[0]

for i in (range(1, length -1)):
    name[i] = ',' + name[i] + ','
if length != 0:
    name[length] = "and " + name[length]

print("Adieu, adieu,",*name)   
