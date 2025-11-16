import random

print("\n\n\n                                       Welcome to the game !  STONE PAPER SCISSOR ")
print()
user= input("Enter your name: ")
match_no = 1

with open ('stone data.txt' , 'a') as f:
    f.write(f"-------------------STONE PAPER SCISSOR GAME--------------------------")
    f.write(f"\n\nuser name: {user}")

while True:
    no_of_round = int(input("Enter no of round you want to play: "))
    print()
    with open ('stone data.txt' , 'a') as f:
         f.write(f"\n\n\n                        MATCH NUMBER {match_no}")
         f.write(f"\n\n NO OF ROUNDS THAT WILL BE PLAYED : {no_of_round}")
    choices = ["stone" , "paper" , "scissor"]

    user_score = 0
    bot_score = 0
    round = 1

    while round < no_of_round+1:
        print(f"------Round {round} ------\n")
        user_choice = input("Enter your choice (stone/paper/scissor) : ").strip().lower()
        if user_choice not in choices:
            print("Invalid input try again")
            continue
        bot_choice = random.choice(choices)
        print(f"you choose: {user_choice}")
        print(f"bot choose: {bot_choice}\n")
        
        if user_choice == bot_choice:
            print("It's a tie!\n")
            continue
        if (bot_choice == "scissor" and user_choice == "paper") or (bot_choice == "paper" and user_choice == "stone") or (bot_choice == "stone" and user_choice == "scissor"):
            bot_score += 1
            print(f"Bot wins round {round}\n") 
            with open ("stone data.txt" , "a") as f:
                f.write(f"\n\nBot wins round {round}")
                f.write(f"\nUser current score: {user_score}")
                f.write(f"\nbot current score: {bot_score}")
        else:
            user_score += 1 
            print(f"You win round {round}\n")
            with open ("stone data.txt" , "a") as f:
                f.write(f"\n\nUser wins round {round}")
                f.write(f"\nUser current score: {user_score}")
                f.write(f"\nbot current score: {bot_score}")
        round += 1

    print("                                               Match Over\n")
    print(f"                                              Your score : {user_score}")
    print(f"                                              Bot score : {bot_score}\n")

    if user_score > bot_score:
        print("\n                                          CONGRATULATIONS!!!.....You won this match\n")
        with open ("stone data.txt" , "a") as f:
                f.write(f"\n\n\n                   User wins the match {match_no} with leading point {user_score - bot_score}")

    elif user_score == bot_score:
        print("\n                                          IT'S A TIE \n")
        with open ("stone data.txt" , "a") as f:
                f.write(f"\n\n\n                   It's a tie with both having point {user_score}")

    else:
        print("\n                                          Uh oh ! Bot wins\n")
        with open ("stone data.txt" , "a") as f:
                f.write(f"\n\n\n                   Bot wins the match {match_no} with leading point {bot_score - user_score}")

    next_match = input("Do you want to play next match (yes/no): ").lower()
    if next_match!= "yes":
        break
    else:
         match_no += 1
 