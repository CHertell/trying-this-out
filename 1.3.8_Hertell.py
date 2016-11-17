from __future__ import print_function
import random

def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')




def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''Summarize the function in this docstring.
    
    Provide descriptions for the arguments and say what type each one is.
    Describe the type and meaning of the value returned.
    '''
    winner = random.choice(players) 

    ####
    # Summarize the following section of code here
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # explain index here
        print(p+', ', end='')
    print(players[len(players)-1]) # explain this line here

    ####
    # Summarize the following section of code here
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    

 
def goguess():
    maxval = 6000
    minval = 1
    answer = random.randint(minval, maxval)
    print('I have a number between ' + str(minval) + ' and ' + str(maxval) + '. ')
    guess = int(raw_input("Guess: ")) 
    count = 1                        
    while not (guess == answer): 
        if guess <= maxval and guess >= minval:
            if guess < answer:
                print(str(guess) + ' is too low.')
            else:
                print(str(guess) + ' is too high.') 
            count += 1 
        else:
            if guess > maxval:   
                print(str(guess) + ' is higher than ' + str(maxval) + '.')
            else:
                print(str(guess) + ' is lower than ' + str(minval) + '.')
        guess = int(raw_input('Guess: '))
    print('Good job, you guessed the number was ' + str(answer) + ' in ' + str(count) + ' tries.') 