# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: naked twins are a situation that there is 2 box in a unit which both of them has ONLY options for digit a and/or b. In this case, it's obvious that either of this 2 box will have a and the other one will have b. this situation is not detected with Only choice or elimination strategy. but by considering that, we can eliminate this 2 digits form the other boxes in the unit.
by naked twins technique, we can eliminate digits a and b without actually knowing the exact position of them. this elimination caused the other boxes of the unit has the lesser possible domains and that helps to solve the puzzle much faster, as the goal is to eliminate unwanted digits to reach to the answer.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: diagonal sudoku is same as normal sudoku, but it has 2 extra rules. the number on each diagonal also need to be unique. diagonal sudoku is a bit harder as it has more rules, but most of the time it make the solution much faster because more rules means more elimination, and more elimination means make the possible domain for each boxes, even smaller.
in order to solve diagonal sudoku, in each round of elimination/only choice/naked twins, we need to consider the diagonals as a seperate units. if we consider them as separate units, then diagonal sudoku can be solved by normal sudoku solver.

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.