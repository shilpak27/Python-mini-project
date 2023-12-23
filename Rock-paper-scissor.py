"""
Workflow of Project
1.input from User(Rock,Paper,Scissor)
2.Computer choice (Computer will choose randomly not conditionally)
3.Result Print

Cases: 
A-rock
rock-rock=tie
rock-paper=paper win
rock-scissor=rock win

B-paper
paper-paper=tie
paper-rock=paper win
paper-scissor=scissor

C-scissor
scissor-scissor=tie
scissor-rock=rock
scissor-paper=scissor
"""
import random
item_list = ("Rock", "paper", "scissor")
user_choice = input("Enter your move= Rock,paper,scissor= ")
comp_choice = random.choice(item_list)

# f-your can print random variables inbetween
print(f"user choice={user_choice},Computer Choice= {comp_choice}")
if user_choice == comp_choice:
    print("both chooses Same: Match Tie")
elif user_choice == "Rock":
    if comp_choice == "paper":
        print("Paper covers Rock= Computer Win")
    else:
        print("Rock Smashes Scissor= You win")

elif user_choice == "Paper":
    if comp_choice == "scissor":
        print("Scissor cuts Paper, Computer Win")
    else:
        print("paper covers rock,you win")

elif user_choice == "scissor":
    if comp_choice == "paper":
        print("scissor cuts paper, you win")
    else:
        print("Rock Smashes scissor,computer win")
