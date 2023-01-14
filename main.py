# Fabien Thich & Dillan Do
# November 30, 2022

import random

word = [ 
  ['Sports','soccer', 'basketball', 'football', 'baseball', 'chess', 'badminton', 'swimming', "handball", "curling", 'golf'],
  
  ['Food', 'apple', 'pear', 'chicken', 'beef', 'pig', 'turkey', 'banana', 'grape', 'grapefruit', 'popsicle'],
  
  ['Countries', 'canada', 'england', 'australia', 'vietnam', 'china', 'russia', 'ukraine', 'mexico', 'greece', 'denmark'],

  ['Car Brands', 'acura', 'buick', 'chevrolet', 'cadillac', 'bmw', 'audi', 'tesla', 'honda', 'volvo', 'porsche'],

  ['Tech Company', 'apple', 'alphabet', 'microsoft', 'meta', 'dell', 'intel', 'ibm', 'hp', 'samsung', 'asus'],

  ['Clothing Company', 'nike', 'gucci', 'chanel', 'adidas', 'zara', 'cartier', 'uniqlo', 'dior', 'rolex', 'puma'],

  ['School Subjects', 'functions', 'physics', 'fitness', 'chemistry', 'biology', 'english', 'french', 'coop', 'robotics', 'photography'],

  ['Music Genre', 'rock', 'jazz', 'funk', 'dubstep', 'electro', 'disco', 'techno', 'rap', 'latin', 'classical'],

  ['Office Items', 'pencil', 'pen', 'computer', 'book', 'desk', 'chair', 'paper', 'stapler', 'printer', 'telephone'],

  ['Apps and Websites', 'youtube', 'gmail', 'spotify', 'discord', 'instagram', 'facebook', 'twitter', 'snapchat', 'tiktok', 'whatsapp'],

       ]

# Setting Up The Game Format and Generating Lists and Words and Topics
lettersRemaining = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersUsed = []
guessRemaining = 6
randomTopic = word[random.randint(0,9)] # change 2 to highest array index 
viewersTopic = randomTopic[0] # viewersTopic gives the first item in the list (topic: ie, Sports or Food)
randomWord = randomTopic[random.randint(1,len(randomTopic) -1)] # Generate a random word within that list
print('\nWELCOME TO HANGMAN', '\n', '-' * 35)


loop = True
secretWord = []
for i in range(len(randomWord)):
  secretWord.append("_")
while loop == True:
  print('\nTopic:', viewersTopic)
  print('Secret Word:', secretWord)
  print('Letters Remaining:', lettersRemaining)
  print('Letters Used: ', end='')
  for i in lettersUsed:
    print(i, end='')
  print('\nGuesses Remaining:', guessRemaining)

  # Get User Input
  for i in range(6):
    print('-' * 35)
    userGuessLetter = input("Enter a letter (! to guess entire word): ")
    guessRemaining -= 1
    
    if guessRemaining >= 0:
      for i in range(len(randomWord)):
        if userGuessLetter.lower() == randomWord[i]:
          secretWord[i] = userGuessLetter
      count = secretWord.count('_')
      if count == 0:
        print("Congratulations, you win, ", end='')
        loop = False
        playAgain = input("Play again? (Y/N)")
      
        if playAgain.lower() == 'y':
          loop = True
          randomTopic = word[random.randint(0,9)]
          secretWord = []
          for i in range(len(randomWord)):
            secretWord.append("_")
          viewersTopic = randomTopic[0]
          guessRemaining = 6
          lettersUsed = []
          randomWord = randomTopic[random.randint(1,len(randomTopic) -1)]
      lettersUsed.append(userGuessLetter)
      
    elif guessRemaining < 0:
      loop = False
      playAgain = input("You lose, it was play again? (Y/N)")
      
      if playAgain.lower() == 'y':
        loop = True
        randomTopic = word[random.randint(0,9)]
        secretWord = [] 
        randomWord = randomTopic[random.randint(1,len(randomTopic) -1)]
        for i in range(len(randomWord)):
          secretWord.append("_")
        viewersTopic = randomTopic[0]
        guessRemaining = 6
        lettersUsed = []
       
    #For loop that runs for the length of the random word

    # For when user wants to guess full word
    if userGuessLetter == '!':
      userGuessWord = input("Enter the secret word: ")
      if userGuessWord.lower() == randomWord.lower():
        print("Congratulations, that is correct")
        loop = False
      else:
        print("That is incorrect, the correct answer is", randomWord)
        loop = False
      playAgain = input("Would you like to play again? (Y/N) ")
      if playAgain.lower() == 'y':
        loop = True
        randomTopic = word[random.randint(0,9)]
        secretWord = []
        randomWord = randomTopic[random.randint(1,len(randomTopic) -1)]
        for i in range(len(randomWord)):
          secretWord.append("_")
        viewersTopic = randomTopic[0]
        guessRemaining = 6
        lettersUsed = []
      else:
        loop = False
    break
