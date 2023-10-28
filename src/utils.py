import re

def sort_by(string_list, pattern):
    # Create a list to store tuples of (original_string, number) for matching elements
    matches = []

    # Iterate through the strings and add matching tuples to the 'matches' list
    for string in string_list:
        match = re.search(pattern, string)
        if match:
            matches.append((string, int(match.group(1))))

    # Sort the 'matches' list based on the extracted numbers
    sorted_matches = sorted(matches, key=lambda x: x[1])

    # Extract the sorted original strings
    sorted_strings = [match[0] for match in sorted_matches]

    return sorted_strings