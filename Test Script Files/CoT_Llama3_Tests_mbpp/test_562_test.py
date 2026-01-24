import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry"]), 7)

    def test_edge_case_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(Find_Max_Length(["apple"]), 5)

    def test_edge_case_all_elements_of_same_length(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry", "date", "elderberry"]), 7)

    def test_edge_case_all_elements_of_different_lengths(self):
        self.assertEqual(Find_Max_Length(["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]), 7)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            Find_Max_Length("apple")

    def test_invalid_input_non_string_elements(self):
        with self.assertRaises(TypeError):
            Find_Max_Length([1, 2, 3])
