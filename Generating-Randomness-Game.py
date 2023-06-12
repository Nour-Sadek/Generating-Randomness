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

# Imported functions

from itertools import product
from random import choice


# Function(s)


def input_processing(cur_user_input: str) -> str:
    """Return a processed string where every character in <cur_user_input> that
    is not 0 or 1 are filtered out.
    """

    # Check if <cur_user_input> has values other than 0's and 1's and filter
    # out if yes

    if len(cur_user_input) != (cur_user_input.count('0')
                               + cur_user_input.count('1')):

        # First, save the indexes of the characters that aren't 0's and 1's
        unwanted_indexes = []
        index = 0
        for charac in cur_user_input:
            if charac != '0' and charac != '1':
                unwanted_indexes.append(index)
            index = index + 1

        # Second, use list comprehension to save the characters that exclude
        # those indexes
        filtered_user_input_list = [cur_user_input[j]
                                    for j in range(len(cur_user_input))
                                    if j not in unwanted_indexes]

        # Third, make the <filtered_user_input> string from the
        # <filtered_user_input_list> that only includes 0's and 1's
        filtered_input = ''.join(filtered_user_input_list)

    else:
        filtered_input = cur_user_input

    return filtered_input


# Constants

MIN_LEN = 100
ALLOWANCE = 1000
MIN_LEN_TEST = 4

""" Receive the original user input od <MIN_LEN> length (Adopted from Stage 1's
code)
"""

print("Please provide AI some data to learn...")
print("The current data length is 0, " + str(MIN_LEN) + " symbols left")

# Creating the user input string that will continuously update the user's input
# of 0's and 1's until it reaches the MIN_LEN length
final_string = ''

# Create a while loop to continuously record the user's input until <MIN_LEN> is
# reached

while len(final_string) < MIN_LEN:

    print('Print a random string containing 0 or 1: ')
    user_input = input()
    filtered_user_input = input_processing(user_input)

    # Add the filtered string to the final string
    final_string = final_string + filtered_user_input

    # Check if MIN_LEN is reached and ask for more input from the user if not
    current_length = len(final_string)
    left_length = MIN_LEN - current_length
    if current_length < MIN_LEN:
        print('Current data length is ' + str(current_length) + ', '
              + str(left_length) + ' symbols left')

# Printing final string to the console
print('Final data string:')
print(final_string)

"""Analyze user's input to allow predictions (adopted from Stage 2's code)"""

# First, create two dictionaries, <triad_dict_zeros> to store the number of
# times 0 came after a triad and similarly <triad_dict_ones>, with all the
# possible triads as keys, originally with values of 0

list_of_triads = list(product(['0', '1'], repeat=3))
keys_set = {''.join(tup) for tup in list_of_triads}

triad_dict_zeros = dict.fromkeys(keys_set, 0)
triad_dict_ones = dict.fromkeys(keys_set, 0)

# Second, record the number of times 0's and 1's come after a triad in the above
# two dictionaries

i = 0
working_string = final_string

while i < len(working_string) - 3:

    triad = working_string[i:(i + 3)]
    following_char = working_string[i + 3]

    if following_char == '0':
        triad_dict_zeros[triad] += 1
    else:
        triad_dict_ones[triad] += 1

    i = i + 1

""" Prompt the start of the game"""

print("You have $" + str(ALLOWANCE) + '.', "Every time the system successfully",
      "predicts your next press, you lose $1. Otherwise, you earn $1.",
      'Print "enough" to leave the game.', "Let's go!")

"""Start the game! How the program predicts the user's input has been adopted
from Stage 3's code."""

current_allowance = ALLOWANCE

while True:

    final_user_input = ''
    # Save user input

    while len(final_user_input) < MIN_LEN_TEST:

        print("Print a random string containing 0 or 1: ")
        user_input = input()

        if user_input == "enough":
            final_user_input = user_input
            break

        final_user_input = input_processing(user_input)

    if final_user_input == "enough":
        break

    # Predict input beyond the first 3 characters

    predicted_input = ''
    i = 0

    while len(predicted_input) < len(final_user_input) - 3:

        triad = final_user_input[i:(i + 3)]
        counts_of_zeros = triad_dict_zeros[triad]
        counts_of_ones = triad_dict_ones[triad]

        if counts_of_ones == counts_of_zeros:
            predicted_input = predicted_input + choice(['0', '1'])
        elif counts_of_zeros > counts_of_ones:
            predicted_input = predicted_input + '0'
        else:
            predicted_input = predicted_input + '1'

        i = i + 1

    print('predictions: ')
    print(predicted_input)

    # Test the accuracy of the predictor

    total_symbols = len(predicted_input)
    correct_symbols = 0

    user_input_to_compare = final_user_input[3:]
    ind = 0

    for char in user_input_to_compare:
        if predicted_input[ind] == char:
            correct_symbols += 1
        ind = ind + 1

    incorrect_symbols = total_symbols - correct_symbols
    accuracy = round(correct_symbols / total_symbols * 100, 2)
    current_allowance = current_allowance - correct_symbols + incorrect_symbols

    print('Computer guessed ' + str(correct_symbols) + ' out of '
          + str(total_symbols) + " symbols right (" + str(accuracy) + " %)")
    print("Your balance is now $" + str(current_allowance))

print("Game Over!")
