# in python == //
# ask user for their name
name = input("What's your name? ").strip().title()
#name = name.strip().title()
first, last = name.split(" ")

# Capitalize user's name
# name = name.title()
# name = name.capitalize()

#say hello to user
#print("hello,\"AMK\"",name, sep = '', end = '')
print(f"hello, {first}")
#print(name)
