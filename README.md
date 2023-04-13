Project Details
==============================


A-Star Search Project Report
==============================

The 8-puzzle is a well-known game that consists of a board, eight tiles, and an empty tile space. 
Every tile is labeled with a number from one to eight. The game starts with the tiles in random locations 
on the board. These tiles are then able to be moved into the empty space. The goal is to shuffle the tiles 
around where the numbered tiles are in order, and the empty space is in the top right corner. Figure 1 
(Phillips, 2022b) shows a possible start state (labeled Start State) and the final goal state (marked Goal 
State). The goal of this project is to create an 8-puzzle that is then randomized. The board is run through 
an algorithm that solves the puzzle using four unique measures. These measures are then analyzed to 
determine which one is the most effective.


Figure 1
8-Puzzle Board: Example Initial and Goal States


To solve the 8-puzzle, the researcher must first build it. One might assume that building the 
puzzle involves constructing some form of a graphical interface that the AI is then able to manipulate. 
This is not entirely the case. Some form of visual representation needs to be made, but this is only to aid 
the user, not the AI. Instead, functionality is key. The AI must be able to manipulate the puzzle by sliding 
the tiles up, down, left, and right. To do this, the AI always needs to know the location of the empty 
space.

A data structure was created to fulfill these requirements. This structure, built in a Python class, 
uses a board represented as a list of numbers. Zero represents the empty space. The class knows where 
the zero is and can swap the zero with the number adjacent to it (excluding the diagonals). The board is 
given when an instance of the class is created. For this program, an already complete board will always 
be supplied.

If the board is always complete, the AI has nothing to solve. Rectifying this requires the board to 
be mixed. This is done by getting a certain number of moves to perform from the user. An integer from 
which to pseudo-randomly generate actions is also required. Pseudo-random moves will be explained 
later, but for now, one should know that these generated moves get the board as close as possible to 
random. Consider an individual with a physical 8-puzzle game who wants to mix up the board to solve. 
She closes her eyes and then moves the tiles around until she is confident she won’t know how to 
retrace her steps. The program can accomplish this at this point. 

The board is now randomly mixed up and ready to be solved by AI. The algorithm developed to 
accomplish this is called A* (a-star). A* looks for the least-cost solution to the applied problem. In this 
case, least-cost means the solution that takes the least amount of moves to apply. To find the best 
move, the algorithm must traverse through a search tree. Figure 2 (Geeks for Geeks, 2022) shows a 
diagram of a sample 8-puzzle search tree. The top of the tree (the root) is the starting board. Each of the 
four paths leading away from the root is a branch that represents a possible move. With the 8-puzzle, 
there are likely many solutions located on the tree.


Figure 2
8-Puzzle Tree Search Example


If A* searches through the entire search tree, then the number of nodes expanded, and the time 
it will take to complete the search is exponential at the depth of the solution (Phillips, 2022b). The least-move solution becomes impractical to find under these conditions. Instead, A* needs to choose the best 
solution without searching through the entire tree.

Each node on the search tree is given a value. The unexplored move with the lowest value is 
expanded and so on. Any ties are broken by selecting the node that was the more newly considered 
move. The assigned value is based on an equation that sets the node cost equal to the cost so far plus 
the remaining cost to the goal. The remaining cost is not known but can be estimated using a heuristic. A 
heuristic simplifies a problem or is a rule of thumb that reduces the number of options to be expanded 
in difficult problems (Phillips, 2022a).

For this problem, four heuristics will be considered. The first heuristic only considers the cost so 
far. So the estimated distance to the goal is always zero. That is, this ‘heuristic’ applies no heuristic and 
is the baseline to test the rest of the heuristics. The second heuristic counts the number of tiles not in 
their solution state. So, if a move would result in tiles two and seven not being at their goal locations, 
then the cost for that move would be the cost so far plus two (one for each misplaced tile). The third 
heuristic counts how many tiles are not in their correct column and then counts how many are not in 
their required row. A tile may be counted twice if it is not in both the correct row and column. Finally, 
the fourth heuristic measures what is known as Manhattan distance. Manhattan distance is the 
difference between where a tile is now and where it needs to be. It is also known as city-block distance 
because it measures horizontal and vertical distance similar to city blocks and doesn’t consider diagonal 
distance.

After writing the algorithm and the four heuristics, they must be analyzed. Each heuristic is 100 
times. They are tested on 100 different boards that have had 100 random moves done to them. Data on each run is recorded. 
This data includes the depth of the solution in the tree (the number of moves to 
reach the solution), the number of moves that were looked at by the algorithm, and the average 
number of nodes at each level of the tree (branching factor).

It is at this point that pseudo-random moves must be revisited. Recall that the user enters a seed 
for the random move generation when creating these boards. However, these ‘random’ moves aren’t 
completely random. Instead, the given seed causes the unknown algorithm to generate a series of 
numbers. Any specific seed will always generate the same series of numbers. So performing 100 moves 
on a board with a certain seed will always result in the same final board. This allows for a direct 
comparison between heuristics.


Table 1
Descriptive Statistics for the Heuristics

Visited Minimum Median Mean Maximum SD
Heuristic 1 17.00 8348.00 30847.87 212525.00 47855.54
Heuristic 2 5.0 378.50 2637.75 39624.00 6259.12
Heuristic 3 5.0 154.00 786.87 10325.00 1744.42
Heuristic 4 4.0 67.50 219.86 2946.00 436.98
Memory
Heuristic 1 29.00 12385.0 35781.65 182532.00 47489.53
Heuristic 2 9.00 604.0 3866.94 53968.0 8775.42
Heuristic 3 9.00 247.5 1187.17 15053.0 2569.78
Heuristic 4 8.00 113.5 349.28 4529.0 674.80
Depth
Heuristic 1 3.00 15.00 15.59 26.00 4.73
Heuristic 2 3.00 15.00 15.59 26.00 4.73
Heuristic 3 3.00 15.00 15.59 26.00 4.73
Heuristic 4 3.00 15.00 15.59 26.00 4.73
EBF
Heuristic 1 1.59 1.84 1.86 3.07 0.18
Heuristic 2 1.44 1.65 1.52 2.08 0.06
Heuristic 3 1.32 1.61 1.44 2.08 0.08
Heuristic 4 1.27 1.58 1.37 2.00 0.08


As the heuristics increase in value, admissibility becomes a concern. A heuristic is inadmissible if 
it ever overestimates the remaining cost to the goal (Phillips, 2022a). This might result in the algorithm 
finding a solution that is not the least-cost solution or not finding a solution. To test this, descriptive 
statistics were calculated on the depth of the solution shown in Table 1 under "Depth." It is known that 
when the heuristic is set to zero (the first heuristic) it will always find the optimal solution. Comparing 
the other heuristics to the first can help determine if there is evidence that a heuristic is inadmissible. 
Table 1 shows that the descriptive statistics for each heuristic equal those of the first heuristic. This 
would suggest that none of our heuristics overestimate the remaining cost to the goal. From this, there 
is no evidence to suggest that the heuristics are not admissible.

If each heuristic finds the best solution to a given board, then the separation between them is 
the performance. Speed is important when solving exponentially large problems (like A*) and can be 
determined by the number of nodes visited. The maximum number of nodes in the "Visited" section of 
Table 1 for the baseline heuristic is 212,525. This is largely impractical, and each of the other heuristics 
improves on this figure. The fourth heuristic (Manhattan distance) consistently beats out the other 
heuristics on the number of maximum nodes visited, with a maximum of 2946. In the worst case, the 
Manhattan distance heuristic only has the algorithm visit 2946 possible moves, making it more effective 
to use.

Another important aspect of performance is memory usage. As the problem gets bigger and 
bigger, it becomes more difficult to store all the possible moves in memory, making the game more 
likely to be unsolvable. The "Memory" section in Table 1 shows the memory usage of each heuristic. 
Each heuristic's median value is much closer to the minimum than the maximum, suggesting a rightskewed distribution. These distributions have large extreme values, but most of the data is closer to the 
median. Considering this, all the medians of the heuristics beat the baseline considerably, and the 
Manhattan Distance heuristic holds the least minimum, median, and maximum nodes in memory.
The effective branching factor of a node is the average number of children that a node 
produces. The closer the effective branching power is to one, the better the algorithm. This number is 
calculated by taking the depth as the root of the number of expanded nodes (𝑏∗ = √𝑁𝑑). 
The EBF section of Table 1 shows the descriptive statistics for the effective branching factor of each heuristic. 
Once again, the minimum, median, and maximum values for each heuristics beat the previous heuristics and 
the baseline. Taking this and the data from the number of visited nodes into account, it suggests that
each heuristic dominates the heuristics above it. A heuristic dominates another heuristic if both 
heuristics are admissible, and the first heuristic is greater than or equal to the second for every value. 
Without testing every value, the decrease in each the number of nodes visited and the effective 
branching factor for each increasing heuristic suggests that they dominate the heuristics before it, 
making them better than the ones before.

In conclusion, the descriptive statistics suggest that each proposed heuristic is admissible. That 
is, they do not overestimate the cost to the goal. Given this assumption, the heuristics can be compared 
to find the one that performs the best. When comparing the speed and memory usage, the Manhattan 
distance heuristic performed consistently better at holding fewer moves in memory and exploring them 
to find the best sequence to the goal state. Manhattan distance also appears to dominate all the other 
heuristics. In other words, it appears to be greater than or equal to the value given by every other 
heuristic for any move. The evidence would argue in favor of Manhattan distance being the best 
heuristic of the four in finding the least amount of moves to the goal. More research should be done to 
fully compare the four heuristics and confirm the findings presented here.


References
Geeks for Geeks (2022). 8 puzzle Problem using Branch And Bound. https://www.geeksforgeeks.org/8-
puzzle-problem-using-branch-and-bound/
Phillips, J. L. (2022a). Informed Search Strategies [PowerPoint Lecture Slides] 
https://jupyterhub.cs.mtsu.edu/azuread/services/csci4350-materials/private/2022-09-
12_Chapter_3d.pdf
Phillips, J. L. (2022b). Informed Search Strategies 2 [PowerPoint Lecture Slides] 
https://jupyterhub.cs.mtsu.edu/azuread/services/csci4350-materials/private/2022-09-
07_Chapter_3c.pdf


