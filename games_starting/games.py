import random

money = 100

#Write your game of chance functions here

def coin_flip(guess, bet):
  '''
  1st parameter guess: 1 (heads) 2(tails)
  2nd parameter bet: amount of money you are betting
  '''
  flip = random.randint(1, 2)
  if guess == flip:
      return bet * 2
  elif guess != flip:
     return -bet

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
    return bet * 2
  else:
    return -bet
 

def highest_card(bet):
  deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 12, 12, 12, 12]

  player_one_money = 100

  draw_cards = []

  player_one_pick = deck.pop(random.randint(1, len(deck)))
  player_two_pick = deck.pop(random.randint(1, len(deck)))

  draw_cards.append(player_one_pick)
  draw_cards.append(player_two_pick)

  if player_one_pick > player_two_pick:
    return bet * 2
  elif player_two_pick > player_one_pick:
    return -bet 
  else:
    return 0


def roulette(guess, bet):
  numbers = [00, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
  player_one_spin = random.choice(numbers)
  # if player guess for a number
  if player_one_spin == 0 or player_one_spin == 00:
    return -bet
  elif player_one_spin == guess and not player_one_spin == 0 or player_one_spin == 00:
    return bet * 35 

  #if player guess for odd and even
  try:
    if str.lower(guess) == "even" and player_one_spin % 2 == 0 and player_one_spin != 0 and player_one_spin != 00:
      return bet * 2
    elif str.lower(guess) == "odd" and player_one_spin % 2 == 1 and player_one_spin != 0 and player_one_spin != 00:
      return bet * 2
    else:
      return -bet
  except TypeError:
    pass




#Call your game of chance functions here

money += coin_flip(1, 50)
money += cho_han("odd", 25)
money += highest_card(50)
money += roulette("even", 50)

print(money)