PIN = "99999"

print("WELCOME")
entry = input("ENTER YOUR PIN: ")

while entry != PIN:
    print("INCORRECT PIN. TRY AGAIN.")
    entry = input("ENTER YOUR PIN: ")
else: 
  print("PIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")




# 1. How is a while loop similar to an if statement?
# Both can use "AND, OR, NOT" to combine conditions.
# 2. How is a while loop different from an if statement?
# if statement: No iteration; executes once. While loop: Iterates until the condition becomes false.
# 3. What would we have to change in our program if the PIN was stored as an integer rather than a string? For example if it was initialized as PIN = 12345.
# When getting the user's input, convert it to an integer using int().
# 4. Comment out the line entry = input(...) from inside the while loop. What happens? Why?
# The user is prompted to enter the PIN once. If the PIN is incorrect, the program enters an infinite loop. Because if the PIN remains true the loop will run indefinitely.
