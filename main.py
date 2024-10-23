import random

number = []

for n in range(1, 101):
    number.append(n)

# print(number)
user = int(input("Guess a number in 1 to 100 :"))

guess = random.choice(number)

if guess == user:
    print("You won⭐")
else:
    print("You lose😭")
