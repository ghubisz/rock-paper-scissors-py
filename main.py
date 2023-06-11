import random

#print multiline instruction

print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      +"Rock vs Paper-> Paper wins \n"
      +"Rock vs Scissors -> Rock wins \n"
      +"Paper vs Scissors -> Scissors wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    #take the input from the user
    choice=int(input("Enter your choice :"))

    #if any of the condition is true, then returns True


    #looping until user enters invalid input
    while choice >3 or choice <1: 
        choice = int(input('Enter a valid choice please :)'))


    #initializing the value of choice_name variable, according to the choice value
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    #print user choice

    print('User choice is \n', choice_name)
    print('Now its Computers Turn...')

    #Computer chooses randomly any number among 1, 2 and 3. Using randint method of random module

    comp_choice = random.randint(1,3)

    #looping until comp_choice value is equal to the choice value

    while comp_choice == choice:
        comp_choice = random.randint(1,3)

    #initialize value of comp_choice_name, a variable corresponding to the choice value

    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissors'

    print("Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)

    if choice == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"
    
    #conditions for win
    if (choice==1 and comp_choice==2):
        print('paper wins =>', end="")
        result='papeR'
    elif (choice==2 and comp_choice==1):
        print('paper wins =>', end="")
        result='Paper'

    if (choice==1 and comp_choice==3):
        print('Rock wins =>\n', end="")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock wins =>\n', end="")
        result='rock'

    if (choice==2 and comp_choice==3):
        print('Scissors wins=>', end="")
        result='scissors'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins=>', end="")
        result='Rock'

    #printing either user or computer wins or draw

    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")

    #if user input n or N then condition is True
    ans = input().lower
    if ans == 'n':
        break
        

# TODO: you can't get out of the game now
# after coming out of the while loop, print thanks for playing 
print("Thanks for playing")