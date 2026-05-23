#Project 3: String Utilities Library with Testing
#Write a string_utils.py file containing 3 functions:
#reverse_words(s): Reverses the order of words (e.g., "hello world" $\rightarrow$ "world hello")
#count_vowels(s): Counts the number of vowels
#is_palindrome(s): Determines if a string is a palindrome
#Write a test_string_utils.py file to test the 3 functions above using pytest
#Each function must have at least 3 test cases (including normal, edge, and exceptional/error cases)
#Run pytest in the terminal to confirm all tests pass

import pytest

from string_utils import reverse_words, count_vowels, is_palindrome

# Test cases for reverse_words
def test_reverse_words_normal():
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_edge_case():
    assert reverse_words("") == ""
    assert reverse_words(" python ") == "python"

def test_reverse_words_exception():
    with pytest.raises(TypeError):
        reverse_words(123)

# --- Tests for the count_vowels function ---
def test_count_vowels_normal():
    assert count_vowels("hello world") == 3

def test_count_vowels_edge_case():
    assert count_vowels("bcdfgh") == 0
    assert count_vowels("AIE") == 3

def test_count_vowels_exception():
    with pytest.raises(TypeError):
        count_vowels(None)


# --- Tests for the is_palindrome function ---

def test_is_palindrome_normal():
    assert is_palindrome("Radar") is True
    assert is_palindrome("hello") is False

def test_is_palindrome_edge_case():
    assert is_palindrome("Race Car") is True
    assert is_palindrome("") is True 

def test_is_palindrome_exception():
    with pytest.raises(TypeError):
        is_palindrome([])
