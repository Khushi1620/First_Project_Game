'''
1 Snake
-1 Water
0 Gun
'''
import random
print("If you want to play Stone Paper Scissor then press 1 and if you want to play Snake Water and Gun press 0 and if you do not want to play anything then press -1")
playAGame = int(input("Enter your choice here: "))
if playAGame == 0:
      print("Welcome in SNAKE , WATER and GUN game.")
      print("There are 3 choices for players.")
      print("1.'s' or 'S' for Snake")
      print("2.'w' or 'W' for Water")
      print("3.'g' or 'G' for Gun")

      wantPlay = int(input("Enter 1 if you want to play otherwise -1: "))
      computerPoints = 0
      userPoints = 0
      while wantPlay == 1:   
           computer = random.choice([-1 , 0 , 1])  
           user = input("Enter your choice here: ")
           yourDict = {"s":1 , "S":1 , "w":-1 , "W":-1 , "g":0 , "G":0}
           reverseDict = {"1":"snake" , "-1":"Water" , "0":"Gun"}
            
           if user in yourDict:
              you = yourDict[user]
              if you == 1:
                print("You chose: 🐍🐍🐍")
              elif you == 0:
                print("You chose: 🔫🔫🔫")
              else:
                  print("You chose: 🌊🌊🌊")
              if computer == 1:
                print("Computer chose: 🐍🐍🐍")
              elif computer == 0:
                print("Computer chose: 🔫🔫🔫")
              else:
                  print("Computer chose: 🌊🌊🌊")
           else:
               print("Please enter correct input")
           if user in yourDict:
               if computer == you:
                   print("Tie between you and computer")
               elif (computer == -1 and you == 1):
                   print("You win🎉🎉")
                   userPoints += 1
               elif computer == -1 and you == 0:
                   print("You lose😢😢")
                   computerPoints += 1
               elif computer == 1 and you == -1:
                   print("You lose😢😢")
                   computerPoints += 1
               elif computer == 1 and you == 0:
                   print("You win🎉🎉")
                   userPoints += 1
               elif computer == 0 and you == -1:
                   print("You win🎉🎉")
                   userPoints += 1
               else:
                   print("You lose😢😢")
                   computerPoints += 1
           else:
               print("Please enter correct input")
           wantPlay = int(input("Enter 1 if you want to play otherwise -1: "))
      if wantPlay != 1:
          print("Your points are: " , userPoints)
          print("Computer points are: " , computerPoints)
          if userPoints > computerPoints:
              print("You are winner🎉🎉🎉")    
          elif computerPoints == userPoints:
              print("Tie between both players") 
          else:
              print("You lose the game😢😢😢")
              print("Try next time")
elif playAGame == 1:
      print("Welcome in STONE , PAPER and SCISSOR game.")
      print("There are 3 choices for players.")
      print("1.'s' or 'S' for Stone")
      print("2.'p' or 'P' for Paper")
      print("3.'c' or 'C' for Scissor")

      wantPlay = int(input("Enter 1 if you want to play otherwise -1: "))
      computerPoints = 0
      userPoints = 0
      while wantPlay == 1:   
           computer = random.choice([-1 , 0 , 1])  
           user = input("Enter your choice here: ")
           yourDict = {"s":1 , "S":1 , "c":-1 , "C":-1 , "p":0 , "P":0}
            
           if user in yourDict:
              you = yourDict[user]
              if you == 1:
                print("You chose: 💎💎💎")
              elif you == 0:
                print("You chose: 📜📜📜")
              else:
                  print("You chose: ✂✂✂")
              if computer == 1:
                print("Computer chose: 💎💎💎")
              elif computer == 0:
                print("Computer chose: 📜📜📜")
              else:
                  print("Computer chose: ✂✂✂")
           else:
               print("Please enter correct input")
           if user in yourDict:
               if computer == you:
                   print("Tie between you and computer")
               elif (computer == -1 and you == 1):
                   print("You win🎉🎉")
                   userPoints += 1
               elif computer == -1 and you == 0:
                   print("You lose😢😢")
                   computerPoints += 1
               elif computer == 1 and you == -1:
                   print("You lose😢😢")
                   computerPoints += 1
               elif computer == 1 and you == 0:
                   print("You win🎉🎉")
                   userPoints += 1
               elif computer == 0 and you == -1:
                   print("You win🎉🎉")
                   userPoints += 1
               else:
                   print("You lose😢😢")
                   computerPoints += 1
           else:
               print("Please enter correct input")
           wantPlay = int(input("Enter 1 if you want to play otherwise -1: "))
      if wantPlay != 1:
          print("Your points are: " , userPoints)
          print("Computer points are: " , computerPoints)
          if userPoints > computerPoints:
              print("You are winner🎉🎉🎉")    
          elif computerPoints == userPoints:
              print("Tie between both players") 
          else:
              print("You lose the game😢😢😢")
              print("Try next time")
else:
    print("Thanks for visiting..!")