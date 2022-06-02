import random


while True:
    user_input = input("Pick an option - R for rock, P for paper, S for scissors: ")
    possible_options = ['R', 'P', 'S'] # list created
    pc_input = random.choice(possible_options)

    # if possible_options.__contains__(user_input):

    if user_input == 'R':
        user_char = 'Rock'
    elif user_input == 'P':
        user_char = 'Paper'  
    elif user_input == 'S':
        user_char = 'Scissors'
    else:
        print('Error in chosen option')
        break
      # print('Sorry, That option does not exist')
      # user_input = input("Pick an option - R for rock, P for paper, S for scissors: ")
        
          

    if pc_input == 'R':
        pc_char = 'Rock'
    elif pc_input == 'P':
        pc_char = 'Paper'  
    else:
        pc_char = 'Scissors'
    
    print(pc_input)
    print(f'\nPlayer({user_char}): CPU({pc_char})')

    if(user_input == pc_input):
      print(f"\n It's a Tie, Both players chose {user_char}")
      print("Do you wan to Play again? YES(Y) or NO(N)")    
      ans = input()
      user_input = input("Pick an option - R for rock, P for paper, S for scissors: ")

      if ans == 'n' or ans == 'N' or ans != 'Y':
        break

    elif user_input == 'R':
      if(pc_input == 'S'):
        print("Rock beats Scissors, You win")
        break
      else:
        print("Paper beats rock, CPU wins")
        break

    elif user_input == 'P':
      if(pc_input == 'R'):
        print("Paper beats Rock, You win")
        break
      else:
        print("Scissors beats paper, CPU wins")
        break  

    elif user_input == 'S':
      if(pc_input == 'P'):
        print("Scissors beats Paper, You win")
        break
      else:
        print("Rock beats Scissors, CPU wins")    
        break

   

    
# user_input = input("Pick an option - R for rock, P for paper, S for scissors: ")
      