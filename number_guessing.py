import random

random_number = random.randint(0,10)

num = int(input("Guess a number between 0 and 10: ").strip())

chances = 0

while chances<2:
    if num == random_number:
        print("congratulations you won!")
        break
    
    else:
        chances +=1
        if num > random_number:
            print("Oops that was a miss, the number is smaller than your guess!")
            print(f"you have {3 - chances} chances left ")
            num = int(input("Try again: ").strip())
        else:
            print("Oops that was a miss, the number is greater than your guess!")
            print(f"you have {3 - chances} chances left ")
            num = int(input("Try again: ").strip())
