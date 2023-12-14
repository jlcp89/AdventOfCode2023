# Open the file "d12_real.txt" for reading
f = open("d12_real.txt")

# Initialize a variable to store the sum of matches
summe = 0

# Function to calculate matches based on the given text and numbers
def matches(text, numbers):
    # Initialize the states string with a dot
    states = "."

    # Expand the states string based on the numbers provided
    for nr in numbers:
        for i in range(int(nr)):
            states += "#"
        states += "."

    # Initialize a dictionary to store state counts
    states_dict = {0: 1}
    new_dict = {}

    # Iterate through each character in the text
    for char in text:
        # Iterate through each state in the current dictionary
        for state in states_dict:
            if char == "?":
                # Handle the case where the character is "?"
                if state + 1 < len(states):
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif char == ".":
                # Handle the case where the character is "."
                if state + 1 < len(states) and states[state + 1] == ".":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]
                if states[state] == ".":
                    new_dict[state] = new_dict.get(state, 0) + states_dict[state]

            elif char == "#":
                # Handle the case where the character is "#"
                if state + 1 < len(states) and states[state + 1] == "#":
                    new_dict[state + 1] = new_dict.get(state + 1, 0) + states_dict[state]

        # Update the states_dict with the new_dict and reset new_dict
        states_dict = new_dict
        new_dict = {}

    # Return the sum of the last two states in the final dictionary
    return states_dict.get(len(states) - 1, 0) + states_dict.get(len(states) - 2, 0)

# Iterate through each line in the file
for line in f.readlines():
    # Split the line into a list of words and remove leading/trailing whitespaces
    line = line.strip().split(" ")

    # Create a text string with 5 times the first word followed by "?"
    text = (5 * (line[0] + "?"))[:-1]

    # Create a list of numbers by repeating each number from the second word 5 times
    numbers = 5 * line[1].split(",")

    # Add the result of matches to the sum
    summe += matches(text, numbers)

# Print the final sum of matches
print(summe)
