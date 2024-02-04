import random 

user_wins = 0
computer_wins = 0

options = ["rock","paper", "scissors"]

while True:
    user_input = input('Type Rock/paper/scissors or Q to quit: ').lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)

    computer_picks = options[random_number]
    print("Computer Picked", computer_picks + ".")

    if user_input == "rock" and computer_picks == "scissors":
        print("You won!")
        user_wins += 1
        continue

    elif user_input == "paper" and computer_picks == "rock":
        print("You won!")
        user_wins += 1
        continue 

    elif user_input == "scissors" and computer_picks == "paper":
        print("You won!")
        user_wins += 1
        continue 
    else:
        print("You lost!")
        computer_wins +=1


print(f"You wins {user_wins} times.")
print(f"computer wins {computer_wins} times.")
print("Goodbye!")



