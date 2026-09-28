import numpy as np

picked_num = round(np.random.rand()*101)
# print(picked_num) 


#loop conditions:
while True:
    guess_num = int(input("Guess a number between 1 to 100: "))

    if guess_num < picked_num:
        print(f"That's less! The number is greater than {guess_num}.")
    elif guess_num > picked_num:
        print(f"That's greater! The number is lesser than {guess_num}.")
    else:
        print(f"Bingoooo! The number is {guess_num}.")
        break

    