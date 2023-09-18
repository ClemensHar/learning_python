import os
import tempfile

import pytest
from pytest import approx


def add(a, b):
    return a + b


def factorial(n):
    """
    Computes the factorial of n.
    """
    if n < 0:
        raise ValueError("received negative input")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def count_word_occurrence_in_string(text, word):
    """
    Counts how often word appears in text.
    Example: if text is "one two one two three four"
             and word is "one", then this function returns 2
    """
    words = text.split()
    return words.count(word)


def count_word_occurence_in_file(file, word):
    count = 0
    with open(file, "r") as f:
        for line in f:
            words = line.split()
            count += words.count(word)
    return count


class WordCounter:
    def __init__(self, text: str = None, filename: str = None):
        self.text = text
        self.filename = filename

    def count_word_occurrence_in_string(self, word):
        """
        Counts how often word appears in text.
        Example: if text is "one two one two three four"
                and word is "one", then this function returns 2
        """
        words = self.text.split()
        return words.count(word)

    def count_word_occurence_in_file(self, word):
        count = 0
        with open(self.filename, "r") as f:
            for line in f:
                words = line.split()
                count += words.count(word)
        return count


############ TESTS ##########
def test_add():
    assert add(0.1, 0.2) == approx(0.3)
    assert add("space", "ship") == "spaceship"


@pytest.mark.parametrize("a, final", [(4, 24), (5, 120), (0, 1)])
def test_factorial(a, final):
    assert factorial(a) == final


def test_count_word_occ_in_string():
    assert count_word_occurrence_in_string("one two one", "one") == 2

    result = count_word_occurrence_in_string("one two one", "one")
    assert type(result) == int
    assert count_word_occurrence_in_string("AAA BBB", "AAA") == 1
    assert count_word_occurrence_in_string("AAA AAA", "AAA") == 2
    # What does this last test tell us?
    # assert count_word_occurrence_in_string('AAAAA', 'AAA') == 1


def test_count_word_occurence_in_file():
    assert count_word_occurence_in_file("word_list.txt", "one") == 4


# TODO seperate test out into second .py file


@pytest.fixture()
def word_counter_setup():
    # define fixture to instatiate class
    wordcounter1 = WordCounter("one two one")
    print("Created wordcounter1 and 2")
    return wordcounter1


def test_count_word_occ_in_string(word_counter_setup):
    assert word_counter_setup.count_word_occurrence_in_string("one") == 2


class TestWordCounter:
    def test_count_word_occ_in_string(self, word_counter_setup):
        assert word_counter_setup.count_word_occurrence_in_string("one") == 2
        wordcounter3 = WordCounter("one two one")
        assert wordcounter3.count_word_occurrence_in_string("one") == 2

    # def test_coung_word_occ_in_file(self):
    #     count = count_word_occurrence_in_file(temporary_file_name, "one")
    #     assert count == 2
