import random 

def roll_dice():
  print (random.randint(1, 6)) 

print("""Welcome to my python random dice program!
To start press enter! Whenever you are over, type quit.""")

flag = True
while flag:
   user_prompt = input(">")
   if user_prompt.lower() == "quit":
      flag = False
   else:
     print("Rolling dice...\nYour number is:",end="") 
     roll_dice()