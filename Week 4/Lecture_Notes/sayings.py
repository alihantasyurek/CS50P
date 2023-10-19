def main():
    hello("world")
    goodbye("world")
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

if __name__ == "__main__": # when you run a file from command line(python saying.py)
    main()                 # python will make __name__ == "__main__"
