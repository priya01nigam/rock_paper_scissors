'''
user      computer   result
rock      paper      computer wins
rock      scissors   rock wins
paper     rock       paper wins
paper     scissors   scissors wins
scissors  paperr     scissors win
scissor   rock       rock win

computer choice=
user_choice
enter your choice=

you win

you lost. comp choose paper

you tied
'''
import random

ch=["Rock","Paper","scissors"]
computer_choice=random.choice(ch)
user_choice=input("type rock, paper or scissors = ").lower()

if user_choice=="rock" and computer_choice=="scissors":
    print("you win")
elif user_choice=="paper" and computer_choice=="rock":
    print("you win")
elif user_choice=="scissors" and computer_choice=="paper":
    print("you win")
elif user_choice==computer_choice:
    print("tie")
else:
    print("you lost, the computer chose", computer_choice)              
