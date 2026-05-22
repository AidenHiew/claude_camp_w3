import pytest
from string_utils import reverse_words, count_vowels, is_palindrome

def test_reverse_words_normal():
    assert reverse_words("hello world") == "world hello"

def test_reverse_words_edge_case():
    assert reverse_words("") == ""
    assert reverse_words(" python ") == "python"

def test_reverse_words_exception():
    with pytest.raises(TypeError):
        reverse_words(123)

def test_count_vowels_normal():
    assert count_vowels("hello world") == 3

def test_count_vowels_edge_case():
    assert count_vowels("bcdfgh") == 0
    assert count_vowels("AIE") == 3

def test_count_vowels_exception():
    with pytest.raises(TypeError):
        count_vowels(None)

def test_is_palindrome_normal():
    assert is_palindrome("Radar") is True
    assert is_palindrome("hello") is False

def test_is_palindrome_edge_case():
    assert is_palindrome("Race Car") is True
    assert is_palindrome("") is True

def test_is_palindrome_exception():
    with pytest.raises(TypeError):
        is_palindrome([])
