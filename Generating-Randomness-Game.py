"""Stage 4: Generate Randomness Game

Description

we will gather all the components from Stages 1 - 3 to construct a game where
you will try to beat the system. Initially, the player has a virtual balance of
$1000. Every time the computer guesses a symbol correctly, the player loses one
dollar. Every time the system is wrong, the player gets one dollar.

Objectives

1 - Print two new lines at the start: "Please provide AI some data to learn...
The current data length is 0, 100 symbols left.

2 - Get and preprocess user input just like in stage 1

3 - Learn the user patterns by collecting triad statistics like in stage 2

4 - Prompt the user to play a game or type "enough" to exit the game. Use the
following phrase: "You have $1000. Every time the system successfully predicts
your next press, you lose $1. Otherwise, you earn $1. Print "enough" to leave
the game. Let's go!

5 - Ask the user to enter random strings, preprocessed to have only 0 and 1
symbols. After preprocessing the string length must be 4, at minimum. If this is
not the case - ask to enter a whole new string. Use this text: "Print a random
string containing 0 or 1: ".

6 - Launch the prediction algorithm and calculate the number of correctly
guessed symbols, like in Stage 3. After each iteration, the remaining balance
is calculated and shown to the user with the message: "Your balance is now $X"
where X is the player's virtual balance.

7 - Finish the game with the words "Game Over!"

"""