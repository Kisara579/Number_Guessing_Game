import random
print("🚀Welcome to Number Guessing Game🚀")

difficulty = input("Choose difficult : Type 'easy' or 'hard' : ").lower()
numbers = []

if difficulty == "easy":
    for number in range(1, 11):
        numbers.append(number)
    user = int(input("Guess a number between 1 to 10 :"))
elif difficulty == "hard":
    for number in range(1, 101):
        numbers.append(number)
    user = int(input("Guess a number between 1 to 100 :"))
# print(numbers)
    
guess = random.choice(numbers)
#print(guess)

if user== guess:
    print("You won⭐")
else:
    print("You lose😭")
