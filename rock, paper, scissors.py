import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if human_choice == 0 or human_choice == 1 or human_choice ==2:
    print(options[human_choice])

    computers_choice = random.randint(0, 2)
    print("Computer's choice is:")
    print(options[computers_choice])

    if human_choice >=3 or human_choice<0:
        print("You typed an invalid number, you lose!")
    elif human_choice == 0 and computers_choice == 2:
        print("You wins!")
    elif computers_choice == 0 and human_choice == 2:
        print("You lose!")
    elif human_choice > computers_choice:
        print("You win!")
    elif computers_choice == human_choice:
        print("It's a draw.")
    elif computers_choice > human_choice:
        print("You lose!")

else:
    print("We're sorry, you made the wrong choice. Please try again!")

