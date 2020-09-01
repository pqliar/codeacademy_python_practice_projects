import random

money = 100

#Write your game of chance functions here

def coin_flip(guess, bet):
  '''
  1st parameter guess: 1 (heads) 2(tails)
  2nd parameter bet: amount of money you are betting
  '''
  money = 100
  flip = random.randint(1, 2)
  print(flip)
  if guess == flip:
      money += bet * 2
      print("Well done, you have won $" + str(bet * 2) + " congratulations!")
  elif guess != flip:
     money = money - bet
     print("Unlucky, you have guessed wrong, you have unfortunately lost $" + str(bet) + ", better luck next time!")
  return money

def cho_han(prediction, bet):
  money = 100
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  result = dice1 + dice2
  result_odd = None
  result_even = None
  if result % 2 == 0:
    result_even = "even"
  else:
    result_odd = "odd"
  if str.lower(prediction) == result_even or str.lower(prediction) == result_odd:
    money += bet * 2
    print("Well done, you have won $" + str(bet * 2) + " congratulations!")
  else:
    money = money - bet
    print("Unlucky, you have guessed wrong, you have unfortunately lost $" + str(bet) + ", better luck next time!")
  return money




#Call your game of chance functions here

coin_flip(1, 50)
cho_han("odd", 25)
