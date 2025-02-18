import random
secrectNumber = random.randint(1, 20)
print("I am thinking number between 1 and 20")

for guessTaken in range (1, 7):
    print("Take a guess")
    guess = int(input())

    if guess < secrectNumber:
        print("Your guess is two low")
    elif guess > secrectNumber:
        print("your guess is two high")
    else:
        break
if guessTaken == secrectNumber:
    print('Good job! You guessed my Number in ' + str(guessTaken) + 'guesses!')
else:
    print('Nope. The number i was thinking was' + str(secrectNumber) )
