import unittest
from mbpp_418_code import Find_Max

class TestFind_Max(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Find_Max([1, 2, 3, 4, 5]), 5)

    def test_edge_case_empty_list(self):
        self.assertRaises(ValueError, Find_Max, [])

    def test_edge_case_single_element_list(self):
        self.assertEqual(Find_Max([10]), 10)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(Find_Max([-5, -3, -1]), -1)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(Find_Max([1, 2, -3, 4, 5]), 5)

    def test_edge_case_duplicates(self):
        self.assertEqual(Find_Max([1, 2, 2, 3, 4, 5]), 5)

    def test_edge_case_non_numeric_input(self):
        with self.assertRaises(TypeError):
            Find_Max(['a', 'b', 'c'])
