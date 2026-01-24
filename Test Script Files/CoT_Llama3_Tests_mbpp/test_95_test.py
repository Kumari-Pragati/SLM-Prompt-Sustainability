import unittest
from mbpp_95_code import Find_Min_Length

class TestFind_Min_Length(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Find_Min_Length(["apple", "banana", "cherry"]), 5)

    def test_edge_case_empty_list(self):
        self.assertEqual(Find_Min_Length([]), 0)

    def test_edge_case_single_element_list(self):
        self.assertEqual(Find_Min_Length(["hello"]), 5)

    def test_edge_case_all_elements_of_same_length(self):
        self.assertEqual(Find_Min_Length(["hello", "world", "hello"]), 5)

    def test_edge_case_all_elements_of_different_lengths(self):
        self.assertEqual(Find_Min_Length(["hello", "world", "abc"]), 3)

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            Find_Min_Length("hello")
