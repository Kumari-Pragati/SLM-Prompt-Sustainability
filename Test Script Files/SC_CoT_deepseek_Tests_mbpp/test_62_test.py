import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5]), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(smallest_num([1]), 1)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5]), -5)

    def test_edge_case_duplicates(self):
        self.assertEqual(smallest_num([5, 5, 5, 5]), 5)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(ValueError):
            smallest_num([])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            smallest_num("1, 2, 3")
