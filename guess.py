import random
print("Hello!, What is your name.?")
my_name = input()
print("Hey, " + my_name + " I am thinking of a number between 1 and 20")
number = random.randint(1, 10)
guess_taken = 0
while guess_taken < 6:
    print("Take a guess.")
    guess = int(input())
    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your guess is to high.")
    if guess == number:
        break
    guess_taken += 1

if guess == number:
    guess_taken = str(guess_taken)

    print("You have guessed the right number." )
if guess != number:
    print("Nope, You have not guessed the right number.")