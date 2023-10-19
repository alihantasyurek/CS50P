import sys

#--------------------------------------------------------------------------------------------------
#Check for errors
#if len(sys.argv) < 2:
    #sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
    #sys.exit("Too many arguments")
##Print name tags
#print("hello, my name is",sys.argv[1])
#--------------------------------------------------------------------------------------------------
#slice > substring[1 is the start and : stands for going to the end]
for arg in sys.argv[1:-1]: #if you do -1 it will count -1 backwards
    print("user>",arg)
