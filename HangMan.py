#Hangman game! guess the word 
import random 
HANGMAN_PICS = ['''
                   ---|---+
                          |
                          |
                          |
                          |
                    ======+ ''','''
                   ---|---+
                      O   |
                          |
                          |  
                          |
                    ======+''' , '''
                   ---|---+
                      O   |
                      |   |
                          |
                          |
                    ======+''' , '''
                   ---|---+
                      O   |
                     /|   |
                          |
                          |
                    ======+ ''' , '''
                   ---|---+
                      O   |
                     /|\  |
                          |
                          |
                    ======+ ''', '''
                   ---|---+
                      O   |
                     /|\  |
                     /    |
                          |
                    ======+ ''', '''
                   ---|---+
                      O   |
                     /|\  |
                     / \  |
                          |
                    ======+ ''']

words = ''' xylophone mnemonic awkward rhythm island subtle receipt debt wristwatch quizzical pokemon jeans zebra 
            stocks market visual studio hangman chronicle schizophrenia pneumonia balloon committe embarrassment necessary
            parallel privilege occurrence mississippi dough ghoul cough wrath gregarious confiscation nvidia jujutsu yacht 
            croissant debris minecraft spider luffy zoro linkedin jigsaw pixel oxygen zigzag blizzard vivid quirk bluff
            flint calendar conscience conscious definite discipline exercise foreign interrupt seperate scratch puzzle jackpot
            knuckle luxury jockey absurd banquet fabric galaxy hybrid jungle insight enigma cactus quartz sphix yolk fragile
            echoes genuine chaos bureau adopt prone brisk latch shard dolphin weird anxious'''.split()

def getRandomWord(words):
    wordIndex = random.randint(0 , len(words)-1) 
    return words[wordIndex]

def displayInfo(correct_letters, missed_letters, secret_word):

    print('Missed letters: ', end= '')
    for letter in missed_letters:
        print(letter, end='')
    print()

    print('Correct letters: ', end= '')
    for letter in correct_letter:
        print(letter, end='')
    print()

    print(HANGMAN_PICS[len(missed_letters)-1])
    print()

    blanks = '_' * len(secret_word)
   

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[ :i] + secret_word[i] + blanks[i+1: ]

    for letter in blanks: 
        print(letter , end='')
    print()

def getGuess(already_Guessed):
    while True: 
        guess = input("Guess a letter: ")
        guess = guess.lower()

        if len(guess) != 1:
            print("Enter a single letter! .")
        elif guess in already_Guessed:
            print("The letter is guessed already enter different letter")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("return a LETTER")
        else: 
            return guess

def playagain():
    print('Do you want to play again ?(yes or no)')
    return input().lower().startswith('y')


print('==== HANGMAN ====')
missed_letter = ' '
correct_letter = ' '
secret_word = getRandomWord(words)
game_completed = False

while True :

    displayInfo(correct_letter , missed_letter , secret_word)

    guess = getGuess(missed_letter + correct_letter)

    if guess in secret_word :
        correct_letter = correct_letter + guess
        foundAllLetters = True
        for i in range(len(secret_word)):
          
          if secret_word[i] not in correct_letter:
            foundAllLetters = False
            break
        if foundAllLetters: 
            print("Cheers! You found the word!, the secret word was " + secret_word + ", You have WON !!")
            game_completed = True
    else: 
            missed_letter = missed_letter + guess

    if len(missed_letter) == (len(HANGMAN_PICS)):
        displayInfo(correct_letter , missed_letter , secret_word)
        print("You ran out of guesses! After =\n " + str(len(correct_letter)) + " correct guesses and \n" + str(len(missed_letter)) + " wrong guesses\n" + "The secret word was: " + secret_word)
        game_completed = True

    if game_completed: 
      if playagain():
          missed_letter = ' '
          correct_letter = ' '
          game_completed = False
          secret_word = getRandomWord(words)
      else:
          break




