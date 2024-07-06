import random

item_list = ("Rock","Paper","Scissor")
playing = True

while playing:

    user_choice = None
    computer_choice = random.choice(item_list)

    while user_choice not in item_list:
        user_choice = input("Enter a choice = Rock,Paper,Scissor = ")

    print(f"User_choice : {user_choice}")
    print(f"computer_choice : {computer_choice}")

    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "Rock" and computer_choice == " Scissors":
        print("The user win!")
    elif user_choice == "Paper" and computer_choice == "Rock":
        print("The user win!")
    elif user_choice == "Scissor" and computer_choice == "Paper":
        print("The user win!")
    else:
        print("The computer win!")

    play_again = input("Do you want to play again?(yes/no): ").lower()
    if not play_again =='yes':
        playing = False

print("Thanks for playing..."