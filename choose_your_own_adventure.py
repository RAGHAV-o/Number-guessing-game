name = input("Type your name: ")
print("welcome", name , "to this adventure!")

answer =input("you are on a dirt road, it has to an end and you can go left or right. which way would you like to go?").lower()
if answer == "left":
    answer = print("You come to a river, you can walk around it and swim accross.Type walk to walk around and swim to swim accross: ").lower()

    if answer == "swim":
        print("You swam accross and were eaten by an alligator, YOU LOSE!")

    if answer == "walk":
        print("You walk many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid input.YOU LOSE!')

elif answer == "right":
    answer = input("You come to a bridge. it looks wobbly, do you want to cross it or head back (cross/back)?: ").lower()
    if answer == "cross":
        answer= input("You cross the bridge and meet a stranger. Do you talk to them (Yes/No)?").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. YOU WIN!")

        elif answer == "no":
            print("You ignore the stranger and they offended, they muderderd you. YOU LOSE!")

        else:
           print('Not a valid input.YOU LOSE!')

    elif answer == "back":
        print("You go back and LOSE!")

    else:
        print('Not a valid input.YOU LOSE!')


else:
    print('Not a valid input.YOU LOSE!')
