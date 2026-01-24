import unittest
from mbpp_772_code import remove_length

class TestRemoveLength(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(remove_length("word word word", 3), "word word")
        self.assertEqual(remove_length("apple banana cherry", 4), "apple banana")

    def test_edge_case_longer_string(self):
        self.assertEqual(remove_length("word word word word", 3), "word word")
        self.assertEqual(remove_length("apple banana cherry orange", 4), "apple banana cherry")

    def test_edge_case_shorter_string(self):
        self.assertEqual(remove_length("word", 3), "")
        self.assertEqual(remove_length("apple", 4), "")

    def test_edge_case_single_word_same_length(self):
        self.assertEqual(remove_length("word", 2), "")
        self.assertEqual(remove_length("apple", 4), "apple")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_length(123, 3)

    def test_invalid_input_negative_k(self):
        with self.assertRaises(ValueError):
            remove_length("word", -1)
