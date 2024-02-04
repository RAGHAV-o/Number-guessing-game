import random 

top_of_range = input("type a number: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print('please type a number again.')
        quit()
else:
    print('please enter a digit next time.')
    quit()

random_number = random.randint(0, top_of_range)
# print(random_number)
guess = 0
while True :
    guess += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
  
    else:
        print('Please enter a digit next time.')
        continue
    if user_guess == random_number:
        print('You guessed it right.')
        break
    
    elif user_guess < random_number:
        print('Number is too small')
    else:
        print('Number is too large')
print("You guessed in ", guess ,"guesses")