import random

user_win = 0
computer_win = 0
opations = ['rock','paper','scissors']


while True:
    user_input = input("enter your choice (rock/paper/scissors) or q for Quit: ").lower()
    if user_input not in opations:
        break

    choice = random.randint(0,2)
    computer_pick = opations[choice]
    print("computer picked: " , computer_pick)

    if user_input ==  computer_pick:
        print("It's a tie")
            
    elif user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_win+=1

    elif user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_win+=1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_win+=1

    else:
        print("You loss!")
        computer_win += 1        

    
print(f"You win {user_win} times.")
print(f"computer win {computer_win} times.")
print("Goodbye!")
