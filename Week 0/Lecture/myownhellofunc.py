def main():
    name = input("name?")
    hello(name)
    hello()

def hello(to="world!"):
    print("hello", to)
