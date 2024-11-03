PIN = "5"

print("I have chosen a number between 1 and 10. Try to guess it.")
entry = input("Your guess: ")

while entry != PIN:
    print("That is incorrect. Guess again.")
    entry = input("Your guess: ")
else: 
  print("That's right! You're a good guesser.")


