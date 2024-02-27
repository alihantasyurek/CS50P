def main():
    name = input("name? ")
    hello(name)
    hello()

def hello(to="world!"): # ="world" is default, don't pass anything = it's gonna print world!
    print("hello", to)

main() #Defining functions != to calling them
