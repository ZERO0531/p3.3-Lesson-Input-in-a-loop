print("I will add up the numbers you give me. ")
      
total = 0
while True:
# Ask user for number
    answer = input("Number: ")
    total = int(input())
    if answer == 0: 
        print(f"The total is {total}.")
    else: 
# Add number to total
        total += answer
        print(f"The total so far is {total}")

