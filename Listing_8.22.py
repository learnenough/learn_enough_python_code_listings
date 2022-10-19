from palindrome.phrase import Phrase
from pytest import skip

def test_non_palindrome():
    assert not Phrase("apple").ispalindrome()

def test_literal_palindrome():
    assert Phrase("racecar").ispalindrome()

def test_mixed_case_palindrome():
    skip()

def test_palindrome_with_punctuation():
    skip()
