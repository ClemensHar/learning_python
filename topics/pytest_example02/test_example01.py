import pytest
from example01 import WordCounter
from pytest import approx


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
