def most_frequent(input_string):
    # Remove spaces and convert the string to lowercase
    input_string = input_string.replace(" ", "").lower()

    # Create a dictionary to store the frequency of each letter
    letter_freq = {}

    # Count the frequency of each letter in the string
    for letter in input_string:
        if letter.isalpha():
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    # Sort the dictionary by frequency in descending order
    sorted_freq = sorted(letter_freq.items(), key=lambda item: item[1], reverse=True)

    # Print the letters and their frequencies in the desired format
    for item in sorted_freq:
        print(f"{item[0]} = {item[1]:02d}", end=" ")

# Input from the user
user_input = input("Please enter a string: ")

# Call the function with the user's input
most_frequent(user_input)
