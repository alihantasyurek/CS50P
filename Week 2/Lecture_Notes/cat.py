#---------------------------------------------------------------------------------------
# while loops
#    i = 0
#    while i < 3:
#        print("meow")
#        i += 1
#
#---------------------------------------------------------------------------------------
# for loops with list
# for i in [0,1,2]:
#    print("meow")
#
#---------------------------------------------------------------------------------------
# for loops with automaticly updated lists
# for _ in range(3):
#    print("meow")
#---------------------------------------------------------------------------------------
# pythonic way to do it
# print("meow\n" * 3, end = "")
#---------------------------------------------------------------------------------------
# My own initial implementation
#n = int(input("What's n? "))
#while n < 0:
#    n = int(input("What's n? "))
#---------------------------------------------------------------------------------------
# common practice when you want a certain values from user
#while True:
#    n = int(input("What's n? "))
#    if n > 0:
#        break
#
#for _ in range(n):
#    print("meow")
#---------------------------------------------------------------------------------------
# same thing with functions
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
       x = int(input("What's number? "))
       if x >= 0:
           return x

def meow(n):
    for _ in range(n): 
        print("meow")
main()
