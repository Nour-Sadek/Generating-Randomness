"""Stage One: Input Processing

Description

To train the machine to predict the next user input, we need to collect data
about the user. We will ask them to press 0's and 1's on the keyboard in an
unpredictable order. These data will be kept in a string of the format
011100101010… Other characters will not be considered. If a user makes a mistake
and presses 2 instead of 1 or enters characters separated by commas, spaces or
any other character — they will be excluded from the input string.

Objectives

1 - Store the value of the minimum length of a string of zeros and ones that the
user must input.
2 - Ask user to enter a random string of 0 and 1.
3 - Read user input and filter out inappropriate symbols from each user input.
4 - Append the processed string to the general string containing all the data
from the inputs.
5 - Keep asking the user for new input strings and appending them to the general
string until the length of the general string is equal to or exceeds the
specified minimum string length.
6 - Output the final data string.

"""

MIN_LEN = 100

# Creating the user input string that will continuously update the user's input
# of 0's and 1's until it reaches the MIN_LEN length
final_string = ''

# Create a while loop to continuously record the user's input until <MIN_LEN> is
# reached

while len(final_string) < MIN_LEN:
    user_input = input('Print a random string containing 0 or 1: ')

    # Check if <user_input> has values other than 0's and 1's and filter out
    # if yes

    if len(user_input) != (user_input.count('0') + user_input.count('1')):

        # First, save the indexes of the characters that aren't 0's and 1's
        unwanted_indexes = []
        i = 0
        for char in user_input:
            if char != '0' and char != '1':
                unwanted_indexes.append(i)
            i = i + 1

        # Second, use list comprehension to save the characters that exclude
        # those indexes
        filtered_user_input_list = [user_input[i]
                                    for i in range(len(user_input))
                                    if i not in unwanted_indexes]

        # Third, make the <filtered_user_input> string from the
        # <filtered_user_input_list> that only includes 0's and 1's
        filtered_user_input = ''.join(filtered_user_input_list)

    else:
        filtered_user_input = user_input

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

"""Stage Two: Analyzing User Input

Description

We will create a "profile" of the user that will contain information about 
patterns found in their "random" clicks. To do this, we will count how many 
times a certain character (0 or 1) follows a specific triad of numbers. Examples 
of triads: 000 or 011. For example, in the string 00010000, the triad 000 is 
followed by a 1 and once by 0.

Objectives

1 - Get all possible triads from the final string. For each of them, count the
number of 0 and 1 that follow them.
2 - Output the result in the following format: [triad: {count_of_0}, 
{count_of_1}], for example, [000: 57, 12]. The result of each triad will be
printed on a new line, ordered in ascending order of their decimal 
representation.

"""
