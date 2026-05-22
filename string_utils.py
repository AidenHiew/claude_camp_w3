#test_string_utils.py

#String_utils.py

def reverse_words(s):
    #check and ensure input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
#split the string into a list of words, reverse the list, and join it back into a string
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

def count_vowels(s):
    #check and ensure input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def is_palindrome(s):
    #check and ensure input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = s.lower().replace(" ", "")
    
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]