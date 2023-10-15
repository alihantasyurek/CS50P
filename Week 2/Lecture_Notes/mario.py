#-------------------------------------------------------------------------------------------------
#def main():
#    print_row(3)
#-------------------------------------------------------------------------------------------------
#    print_column(3)
# def print_column(height):
# one way to print
    # print("#\n" * height, end = "")
# other way to print
#    for _ in range(height): #Range makes it a list that you can use for loop with
#        print("#")
#-------------------------------------------------------------------------------------------------
#def print_row(width):
# print("?" * width)
#-------------------------------------------------------------------------------------------------

# printing 2D brick with nested loops
def main():
    print_square(4)

def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end = "")
        print()
main()
