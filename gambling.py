import random
import time

name = input("Whats your name? ")
bank = 1000

gamble = input("\nWanna Gamble?(Yes/No): ")

while bank > 0 and gamble == "Yes":
  print("\nYou have " + str(bank) + "$")
  dice = int(round(random.uniform(1,6)))

  bid = int(input("\nHow much do you want to bid?: "))
  if bid > bank:
    print("\nYou dont have enough money Lmao")
  else:
    print("\nYour transaction has been passed through")

    your_response = int(input("\nPick a number between 1-6: "))

    print("\nThe dice isss...\n")
    time.sleep(1)
    print(dice)

    if your_response == dice:
      bank += bid*3
      print("\nYou won " + str(bid*5) + "$")
    elif your_response != dice:
      bank -= bid
      print("\nYou lost " + str(bid) + "$")

  print("\nYou now have " + str(bank) + "$")

  if bank <= 0:
    print("\nYou broke now lol")
    exit("Restart?")
  elif bank > 0:
    gamble = input("\nWanna gamble again?(Yes/No): ")
if gamble == "No":
  print("\nOk mommy's boy")

# High Score function was added a month later

p = name + " Scored: " + str(bank)

with open('highScores.txt', 'r') as file:
    highScores = file.read()
    highScores = int(highScores[16:])

if bank > highScores:
  print("\nYou are now 1st place!!!")
  p = name + " Scored: " + str(bank)
  score = int(p[16:])
  with open('highScores.txt',   'w') as file:
    file.write(p)
  with open('highScores.txt',   'r') as file:
    highScores = file.read()
else:
  print("\nYou did not surpass 1st place")
  print("\nFirst place is still whith \n"+p)
  with open('highScores.txt', 'r') as file:
    highScores = file.read()
  print(highScores)
