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

def test_letters():
    assert Phrase("Madam, I'm Adam.").letters() == "MadamImAdam"
