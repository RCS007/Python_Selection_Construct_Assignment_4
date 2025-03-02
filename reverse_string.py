# Problem 4:

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. For example, say I

# type the string:
 # My name is Kalicharan
 
# Then I would see the string:
 # Kalicharan is name My
 
# shown back to me.

# Function to reverse the words in a string
def reverse_words(input_string):
    # Split the string into a list of words
    words = input_string.split()
    # Reverse the list of words and join them back into a string
    reversed_string = ' '.join(reversed(words))
    return reversed_string

# Main program
if __name__ == "__main__":
    # Ask the user for input
    user_input = input("Enter a string with multiple words: ")

    # Get the reversed string
    reversed_output = reverse_words(user_input)

    # Print the reversed string
    print("Reversed string:", reversed_output)
