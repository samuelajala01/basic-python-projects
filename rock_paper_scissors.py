
import random 



while True:
# possible_options.__contains__(user_input):

  user_input = input("Pick an option - R for rock, P for paper, S for scissors: ")

  possible_options = ['R', 'P', 'S']
  pc_input = random.choice(possible_options)
  print(pc_input)

  if user_input == 'R':
      user_char = 'Rock'
  elif user_input == 'P':
      user_char = 'Paper'  
  elif user_input == 'S':
      user_char = 'Scissors'
  else:
      print("Error in chosen option")    

  if pc_input == 'R':
      pc_char = 'Rock'
  elif pc_input == 'P':
      pc_char = 'Paper'  
  else:
      pc_char = 'Scissors'



  if(user_input == pc_input):
    print('Player(',user_char,'): CPU(',pc_char,')')
    print("It's a Tie, Both players selected", user_char )
    break
  elif (user_input == 'R' and pc_input == 'P') or (user_input == 'P' and pc_input == 'R'):
    print('Player(',user_char,'): CPU(',pc_char,')')
    print('Paper beats Rock')
    break
  elif (user_input == 'P' and pc_input == 'S') or (user_input == 'S' and pc_input == 'P'):
    print('Player(',user_char,'): CPU(',pc_char,')')
    print('Scissors beats Paper')
  elif (user_input == 'S' and pc_input == 'R') or (user_input == 'R' and pc_input == 'S'):
    print('Player(',user_char,'): CPU(',pc_char,')')
    print('Rock beats Scissors') 
    break
  else:
    print('No winner')   
    