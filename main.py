import random

finalAnswer = random.randint(1,100)


print('Hello. What is your name?')
name = input()
print('Well, ' + name + " let's play a game.")
print("Guess the number I'm thinking of")
print("Hint: It's been 1 and 100.")

def takeAGuess(): 
  print('Take a guess.') 
  guess = input()
  try:
    totalGuesses = 0
    while totalGuesses < 5:
      totalGuesses += 1 
      if int(guess) < 1 or int(guess) > 100:
        print('That number is not in range')
        takeAGuess()
      else:
          if int(guess) > finalAnswer:
            print('Your guess is too high.')
            takeAGuess()
          elif int(guess) < finalAnswer: 
            print('Your guess is too low.') 
            takeAGuess()
          else:
            break
      if int(guess) == finalAnswer:
          if totalGuesses == 1:
            print('Good job, ' + name + '! You guessed my number in 1 guess!')
          else:
                print('Good job, ' + name + '! You guessed my number in ' + str(totalGuesses) + ' guess!')
      else:    
        print('The number I was thinking of was ' + str(finalAnswer))
      
  except ValueError:
    print('That is not a number')
    takeAGuess()

takeAGuess()
