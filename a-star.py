#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by Cayson Seipel
# September 23, 2022
# This program takes a randomized version of the 8-puzzle and solves it using
# the A* method. A heuristic is applied given user input and diagnostics are printed to
# the console. 

import sys, random, copy, heapq

# Holds the board state and allows the user to perform move the empty tile
class state():
    def __init__(self, tiles, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.tiles = tiles
    def left(self):
        if (self.ypos == 0):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos][s.ypos-1]
        s.ypos -= 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def right(self):
        if (self.ypos == 2):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos][s.ypos+1]
        s.ypos += 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def up(self):
        if (self.xpos == 0):
            return None
        s = self.copy()
        s.tiles[s.xpos][s.ypos] = s.tiles[s.xpos-1][s.ypos]
        s.xpos -= 1
        s.tiles[s.xpos][s.ypos] = 0
        return s
    def down(self):
        if (self.xpos == 2):
            return None
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

# Priority Queue for choosing which board state to expand
class PriorityQueue():
    def __init__(self):
        self.thisQueue = []
    def push(self, thisNode):
        heapq.heappush(self.thisQueue, (thisNode.val, -thisNode.id, thisNode))
    def pop(self):
        return heapq.heappop(self.thisQueue)[2]
    def isEmpty(self):
        return len(self.thisQueue) == 0
    def length(self):
        return len(self.thisQueue)

# Holds information on the node and the parent
nodeid = 0
class node():
    def __init__(self, val, depth, board, parent):
        global nodeid
        self.id = nodeid
        nodeid += 1
        self.val = val
        self.depth = depth
        self.board = board
        self.parent = parent
    def __str__(self):
        return "Node: id=%d val=%d"%(self.id, self.val)
    
# Class for the closed list allows searching through a hash for speed
class Set():
    def __init__(self):
        self.thisSet = set()
    def add(self,entry):
        if entry is not None:
            self.thisSet.add(entry.__hash__())
    def length(self):
        return len(self.thisSet)
    def isMember(self,query):
        return query.__hash__() in self.thisSet
    
# Takes a game board (list of lists) and finds the empty (0) position
def empty_location(game_board):
    for row in range(3):
        if 0 in game_board[row]:
            return row, game_board[row].index(0)

# Expands all possible moves for the current board
def expand_children(parent):
    child_up = parent.up()
    child_down = parent.down()
    child_left = parent.left()
    child_right = parent.right()
    
    return [child_up, child_down, child_left, child_right]

# The heuristic for the a-star algorithm which is chosen though standard input
def heuristic(num, current_state):
    total = 0
    
    if num == 1:
        # Total numbers not in their correct locations
        for row in range(len(current_state)):
            for col in range(len(current_state[row])):
                if current_state[row][col] != (row * 3 + col):
                    total += 1
    elif num == 2:
        # Manhattan distance
        goal_coords = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        
        for row in range(len(current_state)):
            for col in range(len(current_state[row])):
                if current_state[row][col] != 0:
                    total += (abs(goal_coords[current_state[row][col]][0] - row) + 
                              abs(goal_coords[current_state[row][col]][1] - col))
    elif num == 3:
        # Amount of tiles not correct in each row plus the same for each column
        goal_coords = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
        
        for row in range(len(current_state)):
            for col in range(len(current_state[row])):
                if goal_coords[current_state[row][col]][0] != row:
                    total += 1
                
                if goal_coords[current_state[row][col]][1] != col:
                    total += 1
    
    return total
    
def main():
    goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    game = [] # Initial game state
    expanded = 0 # Number of nodes expanded so far
    
    # Read the game in from standard input
    for line in sys.stdin:
        game.append([int(x) for x in line.split()])
        
    if (len(sys.argv) != 2):
        print("Error in", sys.argv[0])
        sys.exit(1)
    else:
        heuristic_num = int(sys.argv[1])
        
    # Create the frontier and closed list
    frontier = PriorityQueue()
    closed_list = Set()
    
    # Add initial state to the frontier
    x, y = empty_location(game)
    first_node = node(heuristic(heuristic_num, game), 0, state(game, x, y), None)
    frontier.push(first_node)
    
    # A* algorithm
    while frontier.isEmpty() != True:
        current_node = frontier.pop()
        expanded += 1
        
        # Check if it is the goal
        if current_node.board.tiles == goal:
            nodes_in_memory = frontier.length() + closed_list.length()
            print_queue = PriorityQueue()
            
            # Print the diagnostics
            print("V=", expanded, sep = "")
            print("N=", nodes_in_memory, sep = "")
            print("d=", current_node.depth, sep = "")
            print("b=", round(nodes_in_memory**(1 / (current_node.depth)), 5), sep = "")
            print()
            
            # Print the solution by adding the steps to the queue and printing in order
            while current_node is not None:
                print_queue.push(current_node)
                current_node = current_node.parent
            
            while print_queue.isEmpty() == False:
                print(print_queue.pop().board)
                
            sys.exit(0)
        
        # Check if the state is not in the closed list and add it
        if closed_list.isMember(current_node.board) == False:
            closed_list.add(current_node.board)
            
            # Expand the children
            children = expand_children(current_node.board)
            
            for child in children:
                if child is not None and closed_list.isMember(child) == False:
                    frontier.push(node(current_node.depth + 1 + heuristic(heuristic_num, child.tiles), 
                                       current_node.depth + 1, child, current_node))
        
main()
