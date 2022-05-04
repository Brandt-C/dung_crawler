from random import sample
from random import choice
import os
CELLS = [
    (0,0),(1,0),(2,0),(3,0),(4,0),
    (0,1),(1,1),(2,1),(3,1),(4,1),
    (0,2),(1,2),(2,2),(3,2),(4,2),
    (0,3),(1,3),(2,3),(3,3),(4,3),
    (0,4),(1,4),(2,4),(3,4),(4,4),
  ]
start_list = sample(CELLS, 7)

cells = {(0, 0): {'disp': '[   ]'}, (1, 0): {'disp': '[   ]'}, (2, 0): {'disp': '[   ]'},
 (3, 0): {'disp': '[   ]'}, (4, 0): {'disp': '[   ]'}, (0, 1): {'disp': '[   ]'}, (1, 1): {'disp': '[   ]'},
  (2, 1): {'disp': '[   ]'}, (3, 1): {'disp': '[   ]'}, (4, 1): {'disp': '[   ]'}, (0, 2): {'disp': '[   ]'},
   (1, 2): {'disp': '[   ]'}, (2, 2): {'disp': '[   ]'}, (3, 2): {'disp': '[   ]'}, (4, 2): {'disp': '[   ]'},
    (0, 3): {'disp': '[   ]'}, (1, 3): {'disp': '[   ]'}, (2, 3): {'disp': '[   ]'}, (3, 3): {'disp': '[   ]'},
     (4, 3): {'disp': '[   ]'}, (0, 4): {'disp': '[   ]'}, (1, 4): {'disp': '[   ]'}, (2, 4): {'disp': '[   ]'},
      (3, 4): {'disp': '[   ]'}, (4, 4): {'disp': '[   ]'}}

def clear():
    os.system('cls')

class Token:
    def __init__(self, pos, disp = '[   ]'):
        self.pos = pos
        self.disp = '[   ]'

    def create_tok(self):
        self.pos = start_list.pop()
    
    def reset_tok(self):
        self.pos = ''
        self.disp = '[   ]'
        

class Player(Token):
    def __init__(self, pos, disp):
        super().__init__(pos, disp)
        self.disp = '[ P ]'
        self.basket = False
        self.win = False

    def create_player(self):
        self.disp = '[ P ]'
        self.basket = False
        self.win = False
        
    def bas_found(self):
        self.disp = '[_P_]'

    def move(self):
        u = input('Where you wanna go? \n\t "w" for up, "s" for down, "a" for left, "d" for right')
        if u == 'w':
            cells[self.pos]['disp'] = '[   ]'
            x = list(self.pos)
            x[1] -= 1
            if x[1] >= 0 and x[1] <= 4:
                self.pos = tuple(x)
            else:
                print('Oh my gosh, you hit a wall!  try again.')
                x[1] += 1
                self.move()
        elif u == 's':
            cells[self.pos]['disp'] = '[   ]'
            x = list(self.pos)
            x[1] += 1
            if x[1] >= 0 and x[1] <= 4:
                self.pos = tuple(x)
            else:
                print('Oh my gosh, you hit a wall!  try again.')
                x[1] -= 1
                self.move()
        elif u == 'a':
            cells[self.pos]['disp'] = '[   ]'
            x = list(self.pos)
            x[0] -= 1
            if x[0] >= 0 and x[0] <= 4:
                self.pos = tuple(x)
            else:
                print('Oh my gosh, you hit a wall!  try again.')
                x[0] += 1
                self.move()
        elif u == 'd':
            cells[self.pos]['disp'] = '[   ]'
            x = list(self.pos)
            x[0] += 1
            if x[0] >= 0 and x[0] <= 4:
                self.pos = tuple(x)
            else:
                print('Oh my gosh, you hit a wall!  try again.')
                x[0] -= 1
                self.move()
    
    def check_move(self):
        
        if self.pos == monster.pos:
            print('The Monster Got You!!!!')
            pass
        else:
            if self.pos == basket.pos:
                self.basket = True
                self.bas_found()
                basket.found()
                print("You got the basket- better go get some eggs!")
            elif self.pos == egg1.pos:
                if self.basket == True:
                    egg1.collected()
                    print('Egg1 collected!')
                else:
                    egg1.found()
                    print("you found an egg- now if you only had a basket to carry it in. . . ")
            elif self.pos == egg2.pos:
                if self.basket == True:
                    egg2.collected()
                    print('Egg2 collected!')
                else:
                    egg2.found()
                    print("you found an egg- now if you only had a basket to carry it in. . . ")
            elif self.pos == egg3.pos:
                if self.basket == True:
                    egg3.collected()
                    print('Egg3 collected!')
                else:
                    egg3.found()
                    print("you found an egg- now if you only had a basket to carry it in. . . ") 
            elif self.pos == door.pos:
                if self.basket == True and egg1.disp == '[ X ]' and egg2.disp == '[ X ]' and egg3.disp == '[ X ]':
                    print("You win!  You win!  You win!  You win!  You win!  You win!  You win!  You win! You win!  You win!\nYou win!  You win!  You win!  You win! You win!  You win!")
                    self.win = True
                else:
                    door.found()
                    print("You found the door! ")


class Monster(Token):
    def __init__(self, pos, disp):
        super().__init__(pos, disp)

    def move(self):
        u = choice(['w', 's', 'a', 'd'])
        if u == 'w':
            x = list(self.pos)
            x[1] -= 1
            if x[1] >= 0 and x[1] <= 4:
                self.pos = tuple(x)
            else:
                x[1] += 1
                self.move()
        elif u == 's':
            x = list(self.pos)
            x[1] += 1
            if x[1] >= 0 and x[1] <= 4:
                self.pos = tuple(x)
            else:
                x[1] -= 1
                self.move()
        elif u == 'a':
            x = list(self.pos)
            x[0] -= 1
            if x[0] >= 0 and x[0] <= 4:
                self.pos = tuple(x)
            else:
                x[0] += 1
                self.move()
        elif u == 'd':
            x = list(self.pos)
            x[0] += 1
            if x[0] >= 0 and x[0] <= 4:
                self.pos = tuple(x)
            else:
                x[0] -= 1
                self.move()
        

class Egg(Token):
    def __init__(self, pos, disp):
        super().__init__(pos, disp)

    def found(self):
        self.disp = '[ 0 ]'

    def collected(self):
        self.disp = '[ X ]'

class Basket(Token):
    def __init__(self, pos, disp):
        super().__init__(pos, disp)

    def found(self):
        self.disp = '[ _ }'

class Door(Token):
    def __init__(self, pos, disp):
        super().__init__(pos, disp)

    def found(self):
        self.disp = '[ / ]'


egg1 = Egg('', '')
egg2 = Egg('', '')
egg3 = Egg('', '')
basket = Basket('', '')
door = Door('', '')
player = Player('', '')
monster = Monster('', '')

class Game:
    def __init__(self):
        pass
        
    def drawMap(self):
        for c in cells:
            if c == egg1.pos:
                cells[c]['disp'] = egg1.disp
            elif c == egg2.pos:
                cells[c]['disp'] = egg2.disp
            elif c == egg3.pos:
                cells[c]['disp'] = egg3.disp
            elif c == basket.pos:
                cells[c]['disp'] = basket.disp
            elif c == door.pos:
                cells[c]['disp'] = door.disp
            elif c == player.pos:
                cells[c]['disp'] = player.disp
        #print(f'{move_count} moves so far.')
        print(cells[(0, 0)]['disp'], cells[(1, 0)]['disp'], cells[(2, 0)]['disp'], cells[(3, 0)]['disp'], cells[(4, 0)]['disp'], "\n")
        print(cells[(0, 1)]['disp'], cells[(1, 1)]['disp'], cells[(2, 1)]['disp'], cells[(3, 1)]['disp'], cells[(4, 1)]['disp'], "\n")
        print(cells[(0, 2)]['disp'], cells[(1, 2)]['disp'], cells[(2, 2)]['disp'], cells[(3, 2)]['disp'], cells[(4, 2)]['disp'], "\n")
        print(cells[(0, 3)]['disp'], cells[(1, 3)]['disp'], cells[(2, 3)]['disp'], cells[(3, 3)]['disp'], cells[(4, 3)]['disp'], "\n")
        print(cells[(0, 4)]['disp'], cells[(1, 4)]['disp'], cells[(2, 4)]['disp'], cells[(3, 4)]['disp'], cells[(4, 4)]['disp'], "\n")
            
    def create_toks(self):
        egg1.create_tok()
        egg2.create_tok()
        egg3.create_tok()
        basket.create_tok()
        door.create_tok()
        player.create_player()
        player.create_tok()
        monster.create_tok()

    def reset(self):
        egg1.reset_tok()
        egg2.reset_tok()
        egg3.reset_tok()
        basket.reset_tok()
        door.reset_tok()
        player.reset_tok()
        monster.reset_tok()
        for c in CELLS:
            cells[c]['disp'] = '[   ]'

    def start(self):
        flag = ''
        while flag != 'q':
            flag = input("Welcome!  You probably know the drill here BUT- 'q' to quit.  Any other key begins the game.")
            if flag == 'q':
                break
            else:
                self.create_toks()
                self.drawMap()
                while player.pos != monster.pos and player.win == False:
                    player.move()
                    clear()
                    monster.move()
                    player.check_move()
                    self.drawMap()
                    continue
                self.reset()
                self.start()