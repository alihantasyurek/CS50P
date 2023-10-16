#------------------------------------------------------------------------------------------------
# My initial thought of handling the Value error 
# x = input("what's x? ")
# while not x.isdigit():
#    x = input("what's x? ")
#    continue
# 
# print(f"x is {int(x)}")
#------------------------------------------------------------------------------------------------
# How to handle an ValueError in Python
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
            #print("X is not integer")
#------------------------------------------------------------------------------------------------
# returning using else statement 
    #while True:
        #try:
            #x = int(input("What's x? "))
        #except ValueError:
            #print("x is not an integer")
        #else: # Execute else if try succeed | if goes in except don't execute else
            #return x
#------------------------------------------------------------------------------------------------
main()
#------------------------------------------------------------------------------------------------
