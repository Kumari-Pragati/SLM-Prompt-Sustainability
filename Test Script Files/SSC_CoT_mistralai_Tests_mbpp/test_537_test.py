import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(first_repeated_word("apple apple banana apple"), "apple")
        self.assertEqual(first_repeated_word("banana blueberry banana"), "banana")
        self.assertEqual(first_repeated_word("apple apple apple"), "apple")

    def test_edge_case_single_word(self):
        self.assertEqual(first_repeated_word("apple"), None)

    def test_edge_case_empty_string(self):
        self.assertEqual(first_repeated_word(""), None)

    def test_edge_case_no_repeated_words(self):
        self.assertEqual(first_repeated_word("apple banana cherry"), None)

    def test_edge_case_repeated_at_end(self):
        self.assertEqual(first_repeated_word("apple apple"), "apple")

    def test_edge_case_repeated_at_beginning(self):
        self.assertEqual(first_repeated_word("apple apple"), "apple")

    def test_edge_case_repeated_in_middle(self):
        self.assertEqual(first_repeated_word("apple apple banana"), "apple")

    def test_edge_case_repeated_multiple_times(self):
        self.assertEqual(first_repeated_word("apple apple apple apple"), "apple")

    def test_edge_case_repeated_with_different_case(self):
        self.assertEqual(first_repeated_word("Apple Apple"), "Apple")

    def test_edge_case_special_characters(self):
        self.assertEqual(first_repeated_word("apple123apple"), None)
        self.assertEqual(first_repeated_word("apple#apple"), None)
        self.assertEqual(first_repeated_word("apple@apple"), None)
