def main():
    if is_even(int(input("The number:"))):
        print("number is odd")
    else:
        print("number is even")

def is_even(x):
    return x % 2

main()
