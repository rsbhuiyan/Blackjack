import random
import art
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
cpu_cards = []
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def check_ace(user, cpu):
  """Function that checks if it needs to change ace from 11 to 1"""
  if 11 in user:
    if total(user) > 21:
      #search for 11 in list
      count = 0
      for i in user:
        if(i == 11):
          user[count] = 1  
        count += 1
  if 11 in cpu:
    if total(cpu) > 21:
      #search for 11 in list
      count = 0
      for i in cpu:
        if(i == 11):
          cpu[count] = 1   
        count += 1
      

def draw_cards(arr):
  """Adds another random card to user or cpu"""
  arr.append(random.randint(0, 12))

def total(arr):
  """Gets total of cards held"""
  total = 0
  for i in arr:
    total += i
  return(total)

  
Y_N = True
#will loop thru game if user wants to play
while(Y_N):
  question = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
  #if user doesnt wanna play exit
  if(question == "n"):
    Y_N = False
  print(art.logo)

  #generate first random cards 
  user_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]] 
  cpu_cards = [cards[random.randint(0, 12)], cards[random.randint(0, 12)]]
  
  check_ace(user_cards, cpu_cards)
  
  
  print(f"Your cards: {user_cards}, current score: {total(user_cards)}")
  print(f"CPU's first card: {cpu_cards[0]}")

  #will loop thru while user wants to keep adding cards or total goes above 21
  userY_N = True
  while(userY_N):
    user_choice = input("\nType 'y' to get another card or type 'n' to pass: ")
    if(user_choice == "y"):
      draw_cards(user_cards)
      draw_cards(cpu_cards)
      userY_N = True
    else:
      while (total(cpu_cards) < 16):
        draw_cards(cpu_cards)
      userY_N = False
      
    check_ace(user_cards, cpu_cards)
    
    print(f"Your cards: {user_cards}, current score: {total(user_cards)}")
    print(f"CPU's first card: {cpu_cards[0]}")

    if(total(user_cards) == 21 or total(cpu_cards) == 21):
      userY_N = False
    elif(total(user_cards) > 21 or total(cpu_cards) > 21):
      userY_N = False
  print(f"\nYour final cards: {user_cards}, final score: {total(user_cards)}")
  print(f"CPU's final cards: {cpu_cards}, final score: {total(cpu_cards)}")
  
  total1 = total(user_cards)
  total2 = total(cpu_cards)
  #check to see final results and print winner
  if(total1 == 21 and total2 == 21):
    print("You Lose! You both got a Blackjack!")
  elif(total1 == 21):
    print("You Win! You got a Blackjack!")
  elif(total2 == 21): 
    print("You Lose! The cpu a Blackjack!")
  elif(total1 > 21):
    print("You Lose! You went over 21")
  elif(total2 > 21):
    print("You Win! Your opponent went over 21")  
  elif(total1 > total2):
    print("You Win! You were closer to 21")
  elif(total1 < total2):
    print("You Lose! CPU was closer to 21")
   
  
      





