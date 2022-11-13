from pytest import skip

from palindrome_mhartl.phrase import Phrase


def test_non_palindrome():
    assert not Phrase("apple").ispalindrome()

def test_literal_palindrome():
    assert Phrase("racecar").ispalindrome()

def test_mixed_case_palindrome():
    assert Phrase("RaceCar").ispalindrome()

def test_palindrome_with_punctuation():
    assert Phrase("Madam, I'm Adam.").ispalindrome()

def test_letters_and_digits():
    assert Phrase("Madam, I'm Adam.").letters_and_digits() == "MadamImAdam"

def test_integer_non_palindrome():
    FILL_IN Phrase(12345).ispalindrome()

def test_integer_palindrome():
    FILL_IN Phrase(12321).ispalindrome()
