import random

size_i, size_j = 10, 10
pole = []
pole2 = []

symbols = {
    'ship' : '[#]', 'damage' : '[*]', 'empty' : '[_]', 'kill' : '[X]', 'miss' : '[-]'
  }

def fill_pole(pole, pole2):
    for i in range(size_i):
        pole.append([])
        for j in range(size_j):
            pole[i].append(symbols['empty'])
    for i in range(size_i):
        pole2.append([])
        for j in range(size_j):
            pole2[i].append(symbols['empty'])    

def pole_battle(user_fight, bot_fight):
    user_fight = [[symbols['empty'] for _ in range(size_j)]for _ in range(size_i)]         
    bot_fight = [[symbols['empty'] for _ in range(size_j)]for _ in range(size_i)]   
    return user_fight, bot_fight    
 
def show_pole(pole):
    cell_width = 5

    print(' '* (cell_width - 1), end = '')
    for j in range(1, size_j + 1):
        print(f'{j:^{cell_width}}', end = '')
    print()

    for i in range(size_i):
         print(f'{i+1:^{cell_width}}', end = '')
         for j in range(size_j):
             print(f'{pole[i][j]:^{cell_width}}', end = '')
         print()    

def show_battle_fields(pole_ships, pole_hits):
    print("Ваши корабли".center(30) + " " * 5 + "Выстрелы по противнику".center(30))
    print("   " + "".join(f"{i+1:3}" for i in range(size_j)) + "     " + "".join(f"{i+1:3}" for i in range(size_j)))
    
    for i in range(size_i):
        row_ships = "".join(f"{cell}" for cell in pole_ships[i])
        row_hits  = "".join(f"{cell}" for cell in pole_hits[i])
        print(f"{i+1:2} {row_ships}     {i+1:2} {row_hits}")         

can_ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
save_user_pole = []
save_bot_pole = []

def save_user(pole, users_ships):
  with open('save_user_pole.txt', 'w') as file:
    for row in pole:
      file.write(''.join(row) + '\n') 
    file.write('users_ships\n')
    file.write(','.join(map(str,users_ships)) + '\n') 

def save_bot(pole2, bot_ships):
  with open('save_bot_pole.txt', 'w') as file: 
    for row in pole2:
      file.write(''.join(row) + '\n')    
    file.write('bots_ships\n')
    file.write(','.join(map(str,bot_ships)) + '\n')     

def dload_game(pole, pole2, users_ships, bot_ships):         
    with open('save_user_pole.txt', 'r') as file:
        lines_user = file.readlines()    

    with open('save_bot_pole.txt', 'r') as file:
        lines_bot = file.readlines()  

    pole.clear()
    pole2.clear()
    users_ships.clear()
    bot_ships.clear()
    section = None

    for line in lines_user:
        line = line.strip()

        if line in ['users_ships']:       
            section = line
            continue

        if section == 'users_ships':
            users_ships = [int(x) for x in line.split(',') if x]
            continue

        cells1 = [cell + ']' for cell in line.split(']') if cell.strip() != '']
        pole.append(cells1)    

    for line in lines_bot:

        if line in ['bots_ships']:           
            section = line
            continue

        if section == 'bots_ships':
            bot_ships = [int(x) for x in line.split(',') if x]
            continue

        cells2 = [cell + ']' for cell in line.split(']') if cell.strip() != '']
        pole2.append(cells2)    


    return pole, pole2 , users_ships, bot_ships

def permit_ships(user_ship, users_ships):
   allowed_user = can_ships.count(user_ship)    
   current_user = users_ships.count(user_ship)  
   if current_user < allowed_user:
      return True
   print('mnogo korabley', (user_ship), '- limit')
   return False

def hand_ships(pole, pole2, users_ships, bot_ships):
    print('#-1; ##-2; ###-3; ####-4')    

    user_ship = int(input('Enter number of ship or 0 for exit and save, 777 for download: ')) 
    if user_ship == 0:
        save_user_pole.append(pole)  
        save_bot_pole.append(pole2) 
        save_user(pole, users_ships)
        save_bot(pole2, bot_ships)
        exit()

    elif user_ship == 777:
        pole, pole2, users_ships, bot_ships = dload_game(pole, pole2, users_ships, bot_ships)
        show_pole(pole)  
        return pole, None, None, None, None, users_ships
    
    print(users_ships)

    if user_ship <= 0 or user_ship > 4:
        print('Error')
        return
    if not permit_ships(user_ship, users_ships):
        return None
    
    while True:
        user_input = input('Enter naklon 1 - horiz, 2 - vertic: ')
        if user_input.isdigit():
            user_angle_ship = int(user_input)
            if user_angle_ship in (1,2):
                break
        print('Enter 1 or 2')

    user_coordinates_i = (int(input('Enter I: ')) - 1)
    if user_coordinates_i < 0 or user_coordinates_i >= size_i:
        print('Error')
        return

    user_coordinates_j = (int(input('Enter J: ')) - 1)
    if user_coordinates_j < 0 or user_coordinates_j >= size_j:
        print('Error')
        return

    if user_angle_ship == 1:
      if user_coordinates_j + user_ship > size_j:
          print('malo mesta')
          return None
      for x in range(user_ship):
          if pole[user_coordinates_i][user_coordinates_j + x] != symbols['empty']:
              return None
    elif user_angle_ship == 2:
      if user_coordinates_i + user_ship > size_i:
          print('malo mesta')
          return None
      for x in range(user_ship):
          if pole[user_coordinates_i + x][user_coordinates_j] != symbols['empty']:
              return None
    return pole, user_angle_ship, user_ship, user_coordinates_i, user_coordinates_j, users_ships


def auto_ships(pole2, bot_ships):
    while len(bot_ships) < len(can_ships):
    
        bot_ship = random.choice(can_ships)

        if bot_ships.count(bot_ship) >= can_ships.count(bot_ship):
            continue
      
        bot_angle_ship = random.randint(1,2)
        bot_coordinates_i = random.randint(0,size_i - 1)
        bot_coordinates_j = random.randint(0,size_j - 1)

        ship_cells = []

         
        if bot_angle_ship == 1:
            if bot_coordinates_j + bot_ship > size_j:
                continue
            ship_cells = [(bot_coordinates_i, bot_coordinates_j + x) for x in range(bot_ship)]
        else:
            if bot_coordinates_i + bot_ship > size_i:
                continue
            ship_cells = [(bot_coordinates_i + x, bot_coordinates_j) for x in range(bot_ship)]

        can_place = True
      
        for i,j in ship_cells:
            for di in [-1,0,1]:
                for dj in [-1,0,1]:
                    ni,nj = i + di, j + dj
                    if 0 <= ni < size_i and 0 <= nj < size_j:
                        if pole2[ni][nj] != symbols['empty']:
                            can_place = False
        if not can_place:
            continue

        for i,j in ship_cells:
            pole2[i][j] = symbols['ship']

        bot_ships.append(bot_ship)

    save_bot_pole.append(pole2)    

    return pole2                         

def can_hand_ships(pole, user_angle_ship, user_ship , user_coordinates_i, user_coordinates_j, users_ships):
    if user_angle_ship == 1:
      for x in range(user_ship):
          pole[user_coordinates_i][user_coordinates_j + x] = symbols['ship']
    else:
      for x in range(user_ship):
          pole[user_coordinates_i + x][user_coordinates_j] = symbols['ship']   
    users_ships.append(user_ship)
    show_pole(pole)
    return True     

def user_put_ships(pole, pole2, users_ships, bot_ships):
    while len(users_ships) < len(can_ships):              
        result = hand_ships(pole, pole2, users_ships, bot_ships)
        if result is None:
            continue

        if result[1] is None:
            pole = result[0]
            pole2 = result[1]
            users_ships = result[5]
            continue
            
        pole, u_a_s, u_s, u_c_i, u_c_j, u_ss = result
        success = can_hand_ships(pole, u_a_s, u_s, u_c_i, u_c_j, u_ss)
        if not success:
            print('ships not OK')
            continue       


      
def user_shoot(pole2, user_fight):
    while True:
      user_i = (int(input('Enter size I: ')) -1)  
      user_j = (int(input('Enter size J: ')) - 1)    

      cell = user_fight[user_i][user_j]

      if cell in (symbols['damage'], symbols['kill'], symbols['miss']):
          print('Уже стрелял сюда')
          continue

      if cell == symbols['ship']:
          user_fight[user_i][user_j] = symbols['damage']

          if is_ship_dead(pole, user_i, user_j):
              mark_dead_ship(pole, user_i, user_j)
              print('Ship is dead')
              continue
          print('Popal')
          continue
      user_fight[user_i][user_j] = symbols['miss']
      print('Mimo')
      break
    

def is_ship_dead(pole, user_i, user_j):
    okr_pole = [(1,0), (-1,0), (0,1), (0,-1)]

    for di, dj in okr_pole:
        x, y = user_i + di, user_j + dj
        while 0 <= x < len(pole) and 0 <= y < len(pole[0]):
            if pole[x][y] == symbols['ship']:
                return False
            if pole[x][y] == symbols['empty'] or pole[x][y] == symbols['miss']:
                break
            x += di 
            y += dj  
    return True         
    
def mark_dead_ship(pole, user_i, user_j):
    okr_pole = [(1,0), (-1,0), (0,1), (0,-1)]     

    pole[user_i][user_j] = symbols['kill']

    for di, dj in okr_pole:
        x, y = user_i + di, user_j + dj
        while 0 <= x < len(pole) and 0 <= y < len(pole[0]):
            if pole[x][y] == symbols['damage']:
                pole[x][y] = symbols['kill']
            else:
                break
            x += di 
            y += dj   

def bot_shoot(pole, bot_fight):
    while True:  

      bot1 = random.randint(0, size_i - 1)
      bot2 = random.randint(0, size_j - 1)

      cell = bot_fight[bot1][bot2]

      if cell in (symbols['damage'], symbols['kill'], symbols['miss']):
          continue
          
      if cell == symbols['ship']:
        bot_fight[bot1][bot2] = symbols['damage']
        print('Popal')
        continue   
      bot_fight[bot1][bot2] = symbols['miss']
      print('Mimo')
      break                          

fill_pole(pole, pole2) 

users_ships = []      
bot_ships = []  
if not bot_ships:
    auto_ships(pole2, bot_ships)  



user_put_ships(pole,pole2, users_ships, bot_ships)
print('-All users ships-')   
save_user(pole, users_ships)
save_bot(pole2, bot_ships)
show_pole(pole)
while True:
    show_battle_fields(pole, user_fight)
    user_shoot(pole2)   
    show_battle_fields(pole2, bot_fight)
    bot_shoot(pole)          