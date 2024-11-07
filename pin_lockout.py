# 1. Change the code so that it locks them out after 4 tries instead of 3. Make sure to change the condition at the bottom, too.
PIN = "12345"
tries = 0

print("WELCOME TO THE BANK OF GALLO.")
entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and tries < 4:
print("\nINCORRECT PIN. TRY AGAIN.")
entry = input("ENTER YOUR PIN: ")
tries += 1

if entry == PIN:
print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries >= 4:
print("\nYOU HAVE RUN OUT OF TRIES. ACCOUNT LOCKED.")

# 2. Make a variable (constant) for the number of maximum tries allowed. Use that variable everywhere instead of just the number.
PIN = "12345"
MAX_TRIES = 4

tries = 0

print("WELCOME TO THE BANK OF GALLO.")

entry = input("ENTER YOUR PIN: ")
tries += 1

while entry != PIN and tries < MAX_TRIES:
print("\nINCORRECT PIN. TRY AGAIN.")
entry = input("ENTER YOUR PIN: ")
tries += 1

if entry == PIN:
print("\nPIN ACCEPTED. YOU NOW HAVE ACCESS TO YOUR ACCOUNT.")
elif tries >= MAX_TRIES:
print(f"\nYOU HAVE RUN OUT OF {MAX_TRIES} TRIES. ACCOUNT LOCKED.")
