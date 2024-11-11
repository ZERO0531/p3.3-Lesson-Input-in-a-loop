print("I have chosen a number between 1 and 10.  Try to guess it.")
answer = input("Your guess: ")

number = "3"
tries = 0

while True: 
    if answer != number:  
        print("That is incorrect. Guess again.")
        tries += 1
        answer = input("Your guess: ")
    else answer == number:
        print("That's right!  You're a good guesser.")
        print(f"It only took you {tries} tries.")
