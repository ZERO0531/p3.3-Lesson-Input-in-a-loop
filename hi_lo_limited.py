# the number 
number = 84
# Initialize number of tries
tries = 1
print("I'm thinking of a number between 1-100.")
print("You have 7 guesses. ")

# Loop
while tries < 7:
# input to the user
    guess = input(f"Guess #{tries}: ")
    tries += 1
# if correct 
    if guess == number:
        print("You guessed it! What are the odds?!? ")
# if too low
    elif guess < number:
        print("Sorry, you are too low.")
# if too high
    else:
        print("Sorry, that guess is too high. ")
# if out of tries
    if tries == 7:
        print("Sorry, you didn't guess it in 7 tries. You lose. ")
        Print(f"The number was {number}. ") 
