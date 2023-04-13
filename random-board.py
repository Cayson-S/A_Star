#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by Cayson Seipel
# September 22, 2022
# This program takes a standard, solved 8-puzzle board as input and returns as
# output a randomized configuration.

import sys, random, copy

class state():
    def __init__(self, tiles, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.tiles = tiles
    def left(self):
        if (self.ypos == 0):
            return self
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos][s.ypos-1]
        s.ypos -= 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def right(self):
        if (self.ypos == 2):
            return self
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos][s.ypos+1]
        s.ypos += 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def up(self):
        if (self.xpos == 0):
            return self
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos-1][s.ypos]
        s.xpos -= 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def down(self):
        if (self.xpos == 2):
            return self
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos+1][s.ypos]
        s.xpos += 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def __hash__(self):
        return (tuple(self.tiles[0]),tuple(self.tiles[1]),tuple(self.tiles[2]))
    def __str__(self):
        return '%d %d %d\n%d %d %d\n%d %d %d\n'%(
                self.tiles[0][0],self.tiles[0][1],self.tiles[0][2],
                self.tiles[1][0],self.tiles[1][1],self.tiles[1][2],
                self.tiles[2][0],self.tiles[2][1],self.tiles[2][2])
    def copy(self):
        s = copy.deepcopy(self)
        return s
    
# This code does not check that the input is a proper board
# or that the input is all integers
# Proper inputs are assumed

def main():
    # Initiate the board and read the board from standard input
    board = []
    
    for line in sys.stdin:
        board.append([int(x) for x in line.split()])
    
    # Read the random seed and number of moves from standard input
    if (len(sys.argv) != 3):
        print("Error in", sys.argv[0])
        sys.exit(1)
    else:
        random.seed(int(sys.argv[1]))
        num_moves = int(sys.argv[2])
    
    # Get the location of the empty space
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                zero_loc = (row, col)
                break
    
    # Instantiate the board as a state that can be manipulated 
    new_board = state(board, zero_loc[0], zero_loc[1])
    
    # Generate moves equal to the number of moves given in input
    for x in range(num_moves):
        # The moves are pseudo-randomly chosen with
        # 0 being up, 1 is right, 2 is down, and 3 is left
        move = random.randrange(4) 
        
        # Move the empty space with the given movement
        if move == 0:
            new_board = new_board.up()
        elif move == 1:
            new_board = new_board.right()
        elif move == 2:
            new_board = new_board.down()
        else:
            new_board = new_board.left()
    
    print(new_board, end = "")

main()

