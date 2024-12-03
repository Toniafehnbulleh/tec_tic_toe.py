"""let's mak;e tec tic toe game"""

import random
import sys

board = [i for in in range(0,9)]
player,computer='',''
moves =((1,7,3,9),(5),(2,4,6,8)) #move for corners,center,other respectively
winners=(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,6),(0,4,8),(2,4,6)#combination for the winner

#table
tab= range (1,10)
def game_board():
    x=1
    for i in board:
        end='|'
        if x%3==0:
            end = '\n'
            if i!=1: end+'_______\n';
            char=''
            if i in ('x','o'):char=i;
            x=1
            print(char,end=end)
            def choose_char():
                chars=('x','o')
                if random.randint(0.1)==0:
                    return chars[::-1]
                return chars
            def can_move(brd,player,move):
                if move in tab and brd[move-1]==move-1:
                    return True

                return False
            def can_win(brd,player,move):
                places =[]
                x=0
                for i in brd:
                    if i ==player:places.append(x);
                    win = True
                    for tip in winners:
                        win=True
                        for ix in tup:
                            if brd [ix]!=player:
                                win=False
                                break
                                if win ==True:
                              break
                               return win
                            def make_move (player,move,undo= False):
                                if can_move (brd,player,move):
                                    brd [move-1]=player
                                    win=can_win(brd,player,move)
                                    if undo:
                                        crd [move-1]=move-1
                                        return (True,False)

                                    #computer moves come here
                                    def comp_moves():
                                   move=-1
                            for i in range(1,10):
                                 if make_move(board,player,i, True)[1]:
                                        move =i
                                        break
                                    if make_move==-1:
                                        for i in range(1,10) #if playercan win,block him
                                            if make_move(board,player,i,True)[1]:
                                                break
                                                if move ==-1:
                                                    for tup in moves: #try to make one off your desired places
                                                        for mv in tup:
                                                            if move ==-1 and can_move (board, computer,mv):
                                                                move=mv
                                                                break
                                                                return make_move(board,computer,move)

                                                            def space_exist():
                                                                return board.count ('x')* board.count('o')!= 9
                                                            plaqyer,computer=chose_char()
                                                            print ('player is [%] and computer is [%s]'%(player,computer))
                                                            result = '%%% Deuce !%%%'
                                                            while space_exist():
                                                                game_board()
                                                                print('#make your move ! [1-9]: ',end='')
                                                                move = int (input() )
                                                                moved , won = make_move (board,player,move)
                                                           if not moved:
                                                               print('>>>invaild number ! try again !')
                                                               continue
                                                               if won :
                                                                   result ='*** Congratulation !You Win!***'
                                                                   break
                                                               elif comp_move()[1]:
                                                                   result = '*** You Loose !***'
                                                                   break
                                                                game_board()







