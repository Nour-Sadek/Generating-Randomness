"""Stage One: Input Processing"""

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

"""Stage Two: Analyzing User Input"""
