import random

def compare:
    if(guess == level):
        print("Just right!")
    elif(guess < level)  
        print("Too little!")
    else:
        print("Too large")

while True:
    try:
        level = int(input("Level: "))
        guess = int(input("Level: "))
        x = random.choice(range(level + 1))
        break
    except (ValueError,IndexError):
        continue

