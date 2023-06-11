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

# First, create two dictionaries, <triad_dict_zeros> to store the number of
# times 0 came after a triad and similarly <triad_dict_ones>, with all the
# possible triads as keys, originally with values of 0

list_of_triads = list(product(['0', '1'], repeat=3))
keys_set = {''.join(tup) for tup in list_of_triads}

triad_dict_zeros = dict.fromkeys(keys_set, 0)
triad_dict_ones = dict.fromkeys(keys_set, 0)

# Second, record the number of times 0's and 1's come after a triad

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

# Uncomment these lines of code if you want to display the statistics in the
# console

# Third, arrange the triads in ascending order

# decimal_binary_dict = {int(value, 2): value for value in keys_set}
# decimals_form_list = [key for key in decimal_binary_dict]

# decimals_form_list.sort()

# Fourth, output the result in the required format

# for decimal_form in decimals_form_list:

#     triad = decimal_binary_dict[decimal_form]
#     counts_of_0 = triad_dict_zeros[triad]
#     counts_of_1 = triad_dict_ones[triad]

#     print(triad + ": " + str(counts_of_0) + ", " + str(counts_of_1))

"""Stage Three: Predicting Future Input

Description

We will make the simplest version of AI to predict the next character of the
user input. We will sequentially scan three characters of the user's sequence
at a time and make a prediction of what goes next.

Objectives

1 - Ask the user to enter another test string of 0 and 1. We'll predict and 
preprocess the new input in the same way as in the first stage, but the minimal 
length of a string is four: 3 characters for prediction, 1 for accuracy 
estimation. If this is not the case — ask to enter a whole new string again.
2 - Going through the string entered by the user, estimate the frequency of
occurrence of 0 or 1 obtained in stage 2 for each triad except the last one, 
and generate predictions. Save the predictions and print them on a new line.
3 - Test the accuracy of the predictor by comparing the real input (without the
first three characters) and the predictions.

"""

MIN_LEN_TEST = 4
final_user_input = ''

# Save user input

while len(final_user_input) < MIN_LEN_TEST:

    user_input = input("Please enter a test string containing 0 or 1: ")
    final_user_input = input_processing(user_input)

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

accuracy = round(correct_symbols / total_symbols * 100, 2)

print('Computer guessed ' + str(correct_symbols) + ' out of '
      + str(total_symbols) + " symbols right (" + str(accuracy) + " %)")
