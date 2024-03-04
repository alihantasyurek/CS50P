str = input("CamelCase: ")
for c in str:
    if c.isupper():
        c = "_", c.lower()
        print("_",c.lower(),sep = "",end="")
        continue
    print(c,sep = "",end="")
