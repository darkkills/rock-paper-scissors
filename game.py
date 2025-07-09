

'''Make a two-player Rock-Paper-Scissors game. One of the players is the computer. 
# Computer will be generating a random number from 1 to 4 using the random module 
# import random
# compChoice= random. randrange (1,4)
# There are 5 chances. Print out the winner and points earned by both players.
# Rock
# Remember the rules:
# • Rock beats scissors
# • Scissors beats paper
# • Paper beats rock
# '''




import random

user_point = 0
comp_point = 0

def scissors(choice, compChoice):
    global user_point, comp_point
    if compChoice == 1:
        print("It's a TIE")
    elif compChoice == 2:
        print("One point for YOU")
        user_point += 1
    elif compChoice == 3:
        print("One point for AI")
        comp_point += 1

def paper(choice, compChoice):
    global user_point, comp_point
    if compChoice == 2:
        print("It's a TIE")
    elif compChoice == 3:
        print("One point for YOU")
        user_point += 1
    elif compChoice == 1:
        print("One point for AI")
        comp_point += 1

def rock(choice, compChoice):
    global user_point, comp_point
    if compChoice == 3:
        print("It's a TIE")
    elif compChoice == 1:
        print("One point for YOU")
        user_point += 1
    elif compChoice == 2:
        print("One point for AI")
        comp_point += 1

def winner():
    print(f"\nFinal Scores: YOU - {user_point}, AI - {comp_point}")
    if comp_point > user_point:
        print("AI WINS!!!!!")
    elif comp_point < user_point:
        print("YOU WIN!!!!!")
    else:
        print("IT'S A TIE")

def game():
    rounds = 0
    while rounds < 5:
        print('''
WELCOME TO ROCK-PAPER-SCISSORS game
Choose your option:
1. SCISSORS
2. PAPER
3. ROCK
4. SHOW WINNER
5. EXIT
''')
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            compChoice = random.randint(1, 3)
            print(f"Computer chose: {compChoice}")
            scissors(choice, compChoice)
            rounds += 1
        elif choice == "2":
            compChoice = random.randint(1, 3)
            print(f"Computer chose: {compChoice}")
            paper(choice, compChoice)
            rounds += 1
        elif choice == "3":
            compChoice = random.randint(1, 3)
            print(f"Computer chose: {compChoice}")
            rock(choice, compChoice)
            rounds += 1
        elif choice == "4":
            winner()
        elif choice == "5":
            print("Exiting .....")
            break
        else:
            print("Invalid choice... please enter a number between 1 and 5.")
    
    print("\nGame Over!")
    winner()

game()
