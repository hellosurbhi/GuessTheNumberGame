import random
import sys

# finalAnswer = random.randint(1,100)
finalAnswer = 50

print('Hello. What is your name?')
name = input()
print('Well, ' + name + " let's play a game.")
print("Guess the number I'm thinking of")
print("It's between 1 and 100 and you have 5 chances to take a guess")
totalGuesses = 0

def takeAGuess(totalGuesses): 
  print('Take a guess.') 
  guess = input()
  try:
    while totalGuesses < 5:
      totalGuesses += 1 
      if int(guess) < 1 or int(guess) > 100:
        print('That number is not in range')
        takeAGuess(totalGuesses)
      else:
          if int(guess) > finalAnswer and totalGuesses<5:
            print('Your guess is too high.')
            takeAGuess(totalGuesses)
          elif int(guess) < finalAnswer and totalGuesses<5: 
            print('Your guess is too low.') 
            takeAGuess(totalGuesses)
      if int(guess) == finalAnswer:
          if totalGuesses == 1:
            print('Good job, ' + name + '! You guessed my number in 1 guess!')
            sys.exit(0)
          else:
                print('Good job, ' + name + '! You guessed my number in ' + str(totalGuesses) + ' guesses!')
                sys.exit(0)
      if totalGuesses == 5:
        if int(guess) != finalAnswer:
          print('The number I was thinking of was ' + str(finalAnswer) + '.')
          print('Better luck next time.')
          sys.exit(0)
  except ValueError:
    print('That is not a number')
    takeAGuess(totalGuesses)

takeAGuess(totalGuesses)

#If you can't import sys then remove line 2(import sys) and change sys.exit(0) to exit(0)
