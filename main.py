# rock paper scissors


import random

print ('===============ROCK,PAPER,SCISSORS================')
# important notice to help users 
# create space make it easy on eyes
print('\n'.strip())
rules = 'please note \n input R for rock, P for paper and S for scissors \n rock beats scissors \n scissors beats paper \n paper beats rock'
print(rules)
# create list to store r rock, p for paper , s for scissors
option = ['R','P','S']
#set i to false
i = False
print('\n'.strip())
while i == False:
    computer_input = random.choice(option)
    print (computer_input)
    #take in user input
    user_input = input(' computer played \n your turn, Rock Paper Scissors?')
    #just to be more user friendly ,accept lower case
    user_input = user_input.upper()
    #set i to true
    i = user_input
    print('\n'.strip())
    #what did the two players choose?  
    if i == 'R':
        if computer_input == 'P':
            print('Player (Rock) : CPU (Paper) ')
        elif computer_input == 'S':
            print('Player (Rock) : CPU (Scissors) ')
    elif i == 'P':
        if computer_input == 'S':
            print('Player (Paper) : CPU (Scissors) ')
        elif computer_input == 'R':
            print('Player (Paper) : CPU (Rock) ')
    elif i == 'S':
        if computer_input == 'P':
            print('Player (Scissors) : CPU (Paper) ')
        elif computer_input == 'R':
            print('Player (Scissors) : CPU (Rock) ')
            print('\n'.strip())
        # who won?
    if (i == 'R' and computer_input == 'P') or (i == 'P' and computer_input == 'S') or (i == 'S' and computer_input == 'R'):
            print ('computer wins') 
            m = input ('do you want to play again? [y/n]')
            if m.lower() == 'y':
                i = False       
    elif (i == 'R' and computer_input == 'S') or (i == 'P' and computer_input == 'R') or (i == 'S' and computer_input == 'P'):
            print ('You won')
            m = input ('do you want to play again? [y/n]')
            if m.lower() == 'y':
                i = False  
    # if its a tie                
    elif i == computer_input:
        print('its a tie')
        i = False
    # invalid input 
    else:
        print('invalid input!!!, please try again')
        i = False
# out of while loop
print ('Bad seeing you leave... \n game ended')
        
    
            
            
            
            