# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:01:02 2019

@author: Mine
"""

#PvP or PvE Tic Tac Toe
import random

class GameBoard():
    game_board = ["\n","_","|","_","|","_","\n","_","|","_","|","_","\n","_","|","_","|","_"]
    
        #start game and clear the board
    def new_game(self):
        self.game_board = ["\n","_","|","_","|","_","\n","_","|","_","|","_","\n","_","|","_","|","_"]
        return print(" ".join(self.game_board))
    
    
    
    
class Player():
    
    
    def __init__(self,name,symbol,cpu_symbol = "?"):
        self.name = name
        self.cpu_symbol = cpu_symbol
        
        #make sure the symbols don't clash
        if symbol != "_" and symbol != cpu_symbol and len(symbol) == 1:
            self.symbol = symbol
        else:
            print("Invalid symbol, we've assigned you X instead")
            self.symbol = "X"
    
        #make moves on the board
    def move(self,spot,GameBoard,cpu = 0):
        if spot >0 and spot <10:
            board_spot = spot*2-1
            if GameBoard.game_board[board_spot] == "_":
                if cpu == 1:
                    GameBoard.game_board[board_spot] = self.cpu_symbol
                else:
                    GameBoard.game_board[board_spot] = self.symbol
                    print(" ".join(GameBoard.game_board))
            else:
                print("That spot is taken, please try again")
        else:
            print("To make a move, please pick either 1,2,3,4,5,6,7,8,or 9,\n which stand for topleft, top middle, topright, and so on.")
        
        # check for victories
        for each in [[1,3,5],[7,9,11],[13,15,17],[1,7,13],[3,9,15],[5,11,17],[5,9,13],[1,9,17]]:
            if GameBoard.game_board[each[0]] == self.symbol and GameBoard.game_board[each[1]] == self.symbol and GameBoard.game_board[each[2]] == self.symbol:
                print("{} is the big winner!".format(self.name))
                GameBoard.new_game()
                
            #check for draw games
        catzgame_counter = 0
        for gamespot in [1,3,5,7,9,11,13,15,17]:
            if GameBoard.game_board[gamespot] != "_":
                catzgame_counter += 1
            if catzgame_counter > 8:
                print("Catz Game!")
                GameBoard.new_game()
    
    
    
    def cpu(self,GameBoard):
        made_a_move = False
                #all the ways a player or the cpu could have victories set up.
        for each in [[1,3,5],[1,5,3],[3,1,5],[3,5,1],[5,1,3],[5,3,1],
                     [7,9,11],[7,11,9],[9,7,11],[9,11,7],[11,7,9],[11,9,7],
                     [13,15,17],[13,17,15],[15,13,17],[15,17,13],[17,13,15],[17,15,13],
                     [1,7,13],[1,13,7],[7,1,13],[7,13,1],[13,1,7],[13,7,1],
                     [3,9,15],[3,15,9],[9,3,15],[9,15,3],[15,3,9],[15,9,3],
                     [5,11,17],[5,17,11],[11,5,17],[11,17,5],[17,5,11],[17,11,5],
                     [5,9,13],[5,13,9],[9,5,13],[9,13,5],[13,5,9],[13,9,5],
                     [1,9,17],[1,17,9],[9,1,17],[9,17,1],[17,1,9],[17,9,1]]:
           
            #is there a way I can win the game this turn?
            if GameBoard.game_board[each[0]] == self.cpu_symbol and GameBoard.game_board[each[1]] == self.cpu_symbol:
                if GameBoard.game_board[each[2]] == "_":
                    GameBoard.game_board[each[2]] = self.cpu_symbol
                    print(" ".join(GameBoard.game_board))
                    made_a_move = True
                    break
                
              #is there a player move I can block?
            elif GameBoard.game_board[each[0]] == self.symbol and GameBoard.game_board[each[1]] == self.symbol:
                    if GameBoard.game_board[each[2]] == "_":
                        GameBoard.game_board[each[2]] = self.cpu_symbol
                        print(" ".join(GameBoard.game_board))
                        made_a_move = True
                        break
                    
                    #make a random move
        if made_a_move == False:
            pick = int(random.randint(1, 9)*2-1)
            if GameBoard.game_board[pick] == "_":
                    GameBoard.game_board[pick] = self.cpu_symbol
                    print(" ".join(GameBoard.game_board))
            else:
                while GameBoard.game_board[pick] != "_":
                    pick = int(random.randint(1, 9)*2-1)
                    if GameBoard.game_board[pick] == "_":
                        pick = int((pick+1)/2)
                        self.move(pick, GameBoard, cpu=1)
                        print(" ".join(GameBoard.game_board))
                        break
        
                #check for victory
        for each in [[1,3,5],[7,9,11],[13,15,17],[1,7,13],[3,9,15],[5,11,17],[5,9,13],[1,9,17]]:
            if GameBoard.game_board[each[0]] == self.cpu_symbol and GameBoard.game_board[each[1]] == self.cpu_symbol and GameBoard.game_board[each[2]] == self.cpu_symbol:
                print("CPU is the big winner!")
                GameBoard.new_game()
                break
            
            #check for draw
        catzgame_counter = 0
        for gamespot in [1,3,5,7,9,11,13,15,17]:
            if GameBoard.game_board[gamespot] != "_":
                catzgame_counter += 1
            if catzgame_counter > 8:
                print("Catz Game!")
                GameBoard.new_game()





