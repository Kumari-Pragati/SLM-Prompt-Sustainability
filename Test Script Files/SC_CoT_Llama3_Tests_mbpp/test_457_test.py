import unittest
from mbpp_457_code import Find_Min

class TestFind_Min(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(Find_Min([]), None)

    def test_edge_case_single_element_list(self):
        self.assertEqual(Find_Min([10]), 10)

    def test_edge_case_list_with_duplicates(self):
        self.assertEqual(Find_Min([1, 2, 2, 3, 4]), 1)

    def test_edge_case_list_with_negative_numbers(self):
        self.assertEqual(Find_Min([-5, -3, -1, 0, 2]), -5)

    def test_edge_case_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            Find_Min([1, 2, 'a', 4, 5])

    def test_edge_case_list_with_non_numeric_values(self):
        with self.assertRaises(TypeError):
            Find_Min([1, 2, 'a', 4, 5.5])
