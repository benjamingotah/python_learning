
maximum = 100
minimum = 0

chosenNumber = __import__('random').randint(0,100)

guessedNumber = int(input('Input your guessed number: '))

if guessedNumber < 0 or guessedNumber > 100: 
    print("Please chose a number between 0-100")

    if guessedNumber < chosenNumber:
        print("It is higher")
    elif guessedNumber > chosenNumber:
        print("It is lesser")
    else:
        print("You've chosen the right number")

