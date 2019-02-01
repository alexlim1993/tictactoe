# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:02:30 2019

@author: Alexander Emmanuel
"""

GAME_BOARD = {(1,1): None, (1,2): None, (1,3): None,
                  (2,1): None, (2,2): None, (2,3): None,
                  (3,1): None, (3,2): None, (3,3): None}

class TTTGameBoard(dict):
    
    def get_box(self, box_number):
        return self[box_number]
    
    def set_box(self, box_number, value):
        self[box_number] = value
    
    def x_ed(self, box_number):
        if self.get_box(box_number) == None:
            self.set_box(box_number, 'crossed')
        else:
            raise "This box is taken!"
    
    def o_ed(self, box_number):
        
        if self.get_box(box_number) == None:
            self.set_box(box_number, 'circled')
        else:
            raise "This box is taken!"
            
    def game_draw(self):
        
        for x in range(1,4):
            for y in range(1,4):
                if self.get_box((x,y)) == None:
                    break
                else:
                    return 'Game is a draw'
            
    def winning(self):
        
        for x in range(1,4):
            if self.get_box((x,1)) == self.get_box((x,2)) and \
            self.get_box((x,1)) == self.get_box((x,3)) and \
            self.get_box((x,1)) != None:
                return self.get_box((x,1)) + ' has won!'
            
            elif self.get_box((1,x)) == self.get_box((2,x)) and \
            self.get_box((1,x)) == self.get_box((3,x)) and \
            self.get_box((1,x)) != None:
                return self.get_box((1,x)) + ' has won!'
            
            else:
                return False
        
        if self.get_box((1,1)) == self.get_box((2,2)) and \
            self.get_box((1,1)) == self.get_box((3,3)) and \
            self.get_box((1,1)) != None:
            return self.get_box((1,1)) + ' has won!'
        
        elif self.get_box((1,3)) == self.get_box((2,2)) and \
            self.get_box((1,3)) == self.get_box((3,1)) and \
            self.get_box((1,3)) != None:
            return self.get_box((1,3)) + ' has won!'
        
        else:
            return False
        
        
#   def starting a new game after a draw or a win
        
class Player:
    
    def __init__(self):
        self._player_1 = 'PLAYER_1'
        self._player_2 = 'PLAYER_2'
           
if __name__ == "__main__":    
    game_board = TTTGameBoard(GAME_BOARD)