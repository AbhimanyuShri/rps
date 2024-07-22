import random

choices=["rock","paper","scissors"]
comp=random.choice(choices)

def choosing():
    while True:
        choose = input("\nWelcome to rock paper scissors! Choose rock, paper or scissors (all lowercase letters): ")
        if choose not in choices:
            print("\nInvalid choice, try again.")
        else:
            return choose

def game_play():
    comp=random.choice(choices)
    choose=choosing()

    if comp == choose:
        print("\nYou and the computer chose " + comp + ". Tie game.")
    elif (choose == "rock" and comp == "scissors") or (choose == "paper" and comp == "rock") or (choose == "scissors" and comp == "paper"):
        print("\nYou chose " + choose + " and the computer chose " + comp + ". You win!")
    else:
        print("\nYou chose " + choose + " and the computer chose " + comp + ". You lose.")
    while True:
        play_again=input("\nWould you like to play again? Type yes or no in all lowercase letters or the question will be asked again.")
        if play_again=="yes":
            game_play()
        elif play_again=="no":
            print("\nThanks for playing!")
        

game_play()
