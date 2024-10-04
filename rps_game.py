import random


def rps(player):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors", 4: "Lizard", 5: "Spock"}

    print("==============================================================")
    print("||    Welcome to Rock, Paper, Scissors Extended version.    ||")
    print("==============================================================")
    print("")
    print(
        "Instructions:\n1. Rock beats Scissors and Lizard.\n2. Paper beats Rock and Spock.\n3. Scissors beats Paper and Lizard.\n4. Lizard beats Spock and Paper.\n5. Spock beats Rock and Scissors."
    )
    print("")

    if player.isdigit():
        player = int(player)
        if player < 1 or player > 5:
            return "Invailid entry, please enter a number between 1-5"

        else:
            player_choice = choices[player]
            computer_num = random.randint(1, 5)
            computer_choice = choices[computer_num]
            # Your choice
            for x, y in choices.items():
                print(f"You chose {player_choice}")
                break

            # Computer's Choice
            for x, y in choices.items():
                print(f"The computer chose {computer_choice}")
                break

            # Results to be Ouputed
            results = ["Its a Draw!", "You Win!", "The Computer Wins!"]

            if computer_choice == player_choice:
                return results[0]
            elif computer_choice == choices[1] and player_choice == choices[2]:
                return results[1]
            elif computer_choice == choices[2] and player_choice == choices[1]:
                return results[2]
            elif computer_choice == choices[1] and player_choice == choices[3]:
                return results[2]
            elif computer_choice == choices[3] and player_choice == choices[1]:
                return results[1]
            elif computer_choice == choices[2] and player_choice == choices[3]:
                return results[1]
            elif computer_choice == choices[3] and player_choice == choices[2]:
                return results[2]
            elif computer_choice == choices[3] and player_choice == choices[4]:
                return results[1]
            elif computer_choice == choices[4] and player_choice == choices[3]:
                return results[2]
            elif computer_choice == choices[4] and player_choice == choices[5]:
                return results[2]
            elif computer_choice == choices[5] and player_choice == choices[4]:
                return results[1]
            elif computer_choice == choices[1] and player_choice == choices[4]:
                return results[2]
            elif computer_choice == choices[4] and player_choice == choices[1]:
                return results[1]
            elif computer_choice == choices[1] and player_choice == choices[5]:
                return results[1]
            elif player_choice == choices[1] and computer_choice == choices[5]:
                return results[2]
            elif computer_choice == choices[2] and player_choice == choices[4]:
                return results[1]
            elif computer_choice == choices[4] and player_choice == choices[2]:
                return results[2]
            elif computer_choice == choices[3] and player_choice == choices[5]:
                return results[1]
            elif computer_choice == choices[5] and player_choice == choices[3]:
                return results[2]
            elif computer_choice == choices[4] and player_choice == choices[3]:
                return results[2]
            elif computer_choice == choices[3] and player_choice == choices[4]:
                return results[1]
            elif computer_choice == choices[2] and player_choice == choices[5]:
                return results[2]
            elif computer_choice == choices[5] and player_choice == choices[2]:
                return results[1]
    else:
        return "Invailid entry! Make sure you enter a number between 1-5."


player = input(
    "Enter 1 for 'Rock', 2 for 'Paper', 3 for 'Scissors', 4 for 'Lizard' or 5 for 'Spock'\n"
)

print(rps(player))
