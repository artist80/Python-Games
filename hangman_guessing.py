#!/usr/bin/env python3

import random
from collections import Counter

someWords = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon 
cherry papaya berry peach lychee muskmelon'''

someWords = someWords.split(' ') 

word = random.choice(someWords) 

def print_word(word, letterGuessed):
    for char in word:
        if char in letterGuessed:
            print(char, end=' ')
        else:
            print('_', end=' ')

def play_game():
    print('Guess the word! HINT: word is a name of a fruit') 

    playing = True
    letterGuessed = '' 
    chances = len(word) + 2
    correct = 0
    flag = 0

    while (chances != 0) and flag == 0: # flag is updated when the word is correctly guessed 
        print() 
        chances -= 1

        try: 
            guess = str(input('Enter a letter to guess: ')) 
        except: 
            print('Enter only a letter!') 
            continue

        # Validation of the guess 
        if not guess.isalpha(): 
            print('Enter only a LETTER') 
            continue
        elif len(guess) > 1: 
            print('Enter only a SINGLE letter') 
            continue
        elif guess in letterGuessed: 
            print('You have already guessed that letter') 
            continue

        # If letter is guessed correctly 
        if guess in word: 
            # k stores the number of times the guessed letter occurs in the word 
            k = word.count(guess) 
            for _ in range(k): 
                letterGuessed += guess # The guess letter is added as many times as it occurs 

        # Print the word 
        print_word(word, letterGuessed)

        # If user has guessed all the letters 
        # Once the correct word is guessed fully, 
        if (Counter(letterGuessed) == Counter(word)): 
            print('Congratulations, You won!') 
            flag = 1
            break # To break out of the while loop 

    # If user has used all of his chances 
    if chances < 0 and (Counter(letterGuessed) != Counter(word)): 
        print() 
        print('You lost! Try again..') 
        print('The word was {}'.format(word)) 

if __name__ == '__main__': 
    play_game()