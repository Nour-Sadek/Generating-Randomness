# Generating Randomness

Prompts the user to play a game where, after "studying" the user's patterns in 
randomly typing 0's and 1's, aims to predict the user's input later, starting 
with a balance of $1000 and the user losing $1 if the program predicts the 
output correctly but gaining $1 if it predicts incorrectly.

# General Info

To learn more about this project, please visit [HyperSkill Website - Generating Randomness Project](https://hyperskill.org/projects/156).

This project's difficulty has been labelled as __Medium__ where this is how 
HyperSkill describes each of its four available difficulty levels:

- __Easy Projects__ - if you're just starting
- __Medium Projects__ - to build upon the basics
- __Hard Projects__ - to practice all the basic concepts and learn new ones
- __Challenging Projects__ - to perfect your knowledge with challenging tasks

This Repository contains two .py files:

    code.py - Contains the code for the first three stages of the project which set the stage for the implementation of the game

    Generating-Randomness-Game.py - Contains the program in which the game should be run

Project was built using python version 3.11.3

# How to Run

Download the files to your local repository and open the project in your choice 
IDE and run the project.

1. You will be prompted to print a random string containing 0 or 1, and will keep being prompted until 
the minimum number of symbols (originally set to 100 but the constant MIN_LEN 
can be changed) have been received. It will be able to handle symbols other 
than 0 or 1.


2. After that, the final string as well as your allowance of $1000 (can 
also be changed, saved under ALLOWANCE constant) will be displayed.


3. You will be prompted to print a random string containing 0 or 1, and will be 
prompted again if the total number of 0's and 1's doesn't exceed 4.


4. After that, the program's prediction as well as your current, updated 
balance will be displayed.


5. Steps 3 and 4 will keep repeating until you type enough, after which the
program's execution ends.
