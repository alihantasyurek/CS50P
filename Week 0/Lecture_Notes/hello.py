# python uses hash(#) for single line comments
"""
 for multi line comments
"""

# ask user for their name
name = input("What's your name? ").strip().title()
first, last = name.split(" ")

# Capitalize user's name
# name = name.title() if start of the word made that word capitilize
# name = name.capitalize() only capitilizes the first letter.

#say hello to user
#print("hello,\"AQ\"",name, sep = '', end = '')
print(f"hello, {first}")
print(f"hello, {last}")
#print(f"hello, {last})
#      format  ,{var chosen to be formatted}
