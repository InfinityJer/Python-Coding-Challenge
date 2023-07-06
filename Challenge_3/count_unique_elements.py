#!/usr/bin/python3i
def count_unique_elements(arr):
    # Initialize an empty set to store unique elements
    unique_elements = set()

    # Iterate through the list and add each element to the set
    for element in arr:
        unique_elements.add(element)

    # Return the count of unique elements
    return len(unique_elements)
