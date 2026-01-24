import unittest
from mbpp_326_code import most_occurrences

class TestMostOccurrences(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = ["hello world", "world is beautiful"]
        self.assertEqual(most_occurrences(test_list), "world")

    def test_edge_case_single_word(self):
        test_list = ["hello"]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_boundary_case_empty_list(self):
        test_list = []
        self.assertIsNone(most_occurrences(test_list))

    def test_boundary_case_all_same_words(self):
        test_list = ["hello hello hello", "hello hello hello"]
        self.assertEqual(most_occurrences(test_list), "hello")

    def test_error_handling_invalid_input(self):
        test_list = ["hello", 123]
        with self.assertRaises(TypeError):
            most_occurrences(test_list)
