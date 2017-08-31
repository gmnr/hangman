# hangman.py - a commandline version of the famous hangman game 
# Guido Minieri - August 2017

from random import choice
from time import sleep


# import the english dictionary to a list
def import_dict():
    global word_list
    word_list = []

    with open('./dictionary.txt') as f:
        for line in f:
            word_list.append(line)


# print statistics
def stats():
    global losses
    print('Your stats are as follows:')
    print('Played: {}'.format(games_played))
    print('Wins: {} - Losses: {}'.format(games_played-losses, losses))
    if losses > 0 and games_played > 0:
        print('Your win ratio is: {}%'.format(round(((games_played - losses)/games_played))*100))
    else:
        print('Your win ratio is: 0.0%')


# hangman pics
try1 = """



___
The gallows.."""

try2 = """

 |
 |
_|_
Nice!"""

try3= """
  ___
 |
 |
_|_
Here it comes.."""

try4= """
  ___
 |  O
 |
_|_
The head!!"""

try5= """
  ___
 |  O
 |  |
_|_
A hot bod.."""

try6= """
  ___
 |  O
 | /|
_|_
Ouch.."""

try7= """
  ___
 |  O
 | /|\\
_|_
This must hurt.."""

try8= """
  ___
 |  O
 | /|\\
_|_/
This is the laast oooonee!"""

try9= """
  ___
 |  O
 | /|\\
_|_/ \\
GAME OVER MATE!!!"""


# create a list with the hangman pics
tries = [None]  # added none so the lists starts from 1
tries.extend(value for name, value in sorted(locals().items(), key=lambda item:item[0]) if name.startswith('try'))


# main
if __name__ == "__main__":

    
    # initialize dictionary
    import_dict()


    # stats tracking
    games_played = 0
    losses = 0


    # main loop
    while True:
        player = input('Do you want to play?  (y/n) [stats to display statistics]\n')
        if player[0] == 'n':
            print('\n')
            print('Ook, have a nice day')
            sleep(1)
            want_stats = input('Print stats?  (y/n)\n')

            if want_stats[0] == 'y':
                stats()
                sleep(3.6)
                print('Quitting...')
                sleep(1.2)
                break

            else:
                print('Quitting...')
                sleep(1.2)
                break

        elif player == 'stats':
            stats()
            print('\n')
            continue

        elif player[0] == 'y':
            print('\n')
            games_played += 1

        else:
            print("Didn't get ya..")
            sleep(0.5)
            print('\n')
            continue
    

        # select the word of the round (and remove final space)
        word = choice(word_list)[:-1]
        print('The word of this round has {} letters..'.format(len(word)))
        sleep(1)


        # start round
        guesses = []
        mistakes = 0
        while True:
            for l in word:

                if l in guesses:
                    print(l, end=' ')

                else:
                    print('_', end=' ')

            player_guess = input('Guess your letter..   (type "help" to show previous letters)\n')
            print('\n')


            # handle wrong input
            if player_guess == 'help':
                print('Your previous guesses have been\n', guesses, '\n\n')

            elif len(player_guess) > 1 or player_guess == '' or player_guess == ' ':
                print('Invalid selection, only one letters allowed.. Try again\n\n')
                sleep(0.7)
                continue

            elif player_guess in guesses:
                print('You have already tried this letter.. Move on!\n\n')
                sleep(0.7)
                continue

            else:
                guesses.append(player_guess)
                if player_guess not in word:
                    mistakes += 1
                    print(tries[mistakes])


            # Victory
            if set([x for x in word]).issubset(guesses):
                print('THE WORD IS:')
                for i in word:
                    print(i, end=' ')
                print('\nYou made it!!')
                print('CONGRATS\n\n')
                break


            # Game over
            if mistakes == 9:
                losses += 1
                print('The word you were trying to guess was:\n{}\n'.format(word))
                break
