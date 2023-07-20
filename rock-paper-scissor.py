# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
s="-"*40
print(s.center(60))
print("Welcome to Rock Paper Scissors".center(60))
print(s.center(60))
print("Rules:\n  1) Rock wins against scissors.\n  2) Scissors win against paper.\n  3) Paper wins against rock.")
throw=[rock,paper,scissors]
print("\nInput:\n 0 for Rock\n 1 for Paper\n 2 for Scissors\n")
while(True):
  choice=int(input("What do you chose? "))
  print("\nYour Choice:")
  print(throw[choice])
  print("Computer Choice:")
  c_choice=random.randint(0,2)
  print(throw[c_choice])
  if choice==0 and c_choice==2:
    print("\"YOU WIN\"")
    break
  elif choice==1 and c_choice==0:
    print("\"YOU WIN\"")
    break
  elif choice==2 and c_choice==1:
    print("\"YOU WIN\"")
    break
  elif choice == c_choice:
    print("\"It's a TIE\"")
    print("\nLet's break this TIE.")
    continue
  elif((choice>2 and choice<0) or (c_choice>2 and c_choice<0)):
    print("Invalid Input.\nEnter your choice in valid range.")
    continue
  else:
    print("\"YOU LOSE\"")
    break