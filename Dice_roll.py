import random 

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value, max_value)
    return roll

while True:
    player = input("Enter the number of player(2-4): ")
    if player.isdigit():
        player = int(player)
        if 2 <= player <= 4:
            break
        else:
            print("player must be between (2-4)")
    else:
        print("Invalid try again!")

max_score = 50
player_score = [0 for _ in range(player)]

while max(player_score) < max_score:

    for player_indx in range(player):
        print("\nplayer number", player_indx +1, "turn has just started!")
        print("Your total score is:", player_score[player_indx] , "\n")
        current_score = 0

        while True:    
            should_roll = input("Would you like to roll (y)? ").lower()
            if should_roll != "y":
                break

            value = roll()
                
            if value == 1:
                current_score = 0
                print("You rolled 1! Turn done.")
                break

            else:
                current_score += value
                print("You rolled a:", value)

            print(f"Your current score is: {current_score}")

        player_score[player_indx] += current_score
        print("Your total score is: ", player_score[player_indx])

max_score = max(player_score)
winning_indx = player_score.index(max_score)
print("player number", winning_indx+1 ,
     "is the winner with score of:", max_score)