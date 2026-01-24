import unittest
from mbpp_457_code import Find_Min

class TestFind_Min(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_edge_case(self):
        self.assertEqual(Find_Min([-1, -2, -3, -4, -5]), -5)

    def test_empty_list(self):
        self.assertRaises(ValueError, Find_Min, [])

    def test_single_element_list(self):
        self.assertEqual(Find_Min([10]), 10)

    def test_list_with_duplicates(self):
        self.assertEqual(Find_Min([1, 2, 2, 3, 4, 5]), 1)

    def test_list_with_negative_numbers(self):
        self.assertEqual(Find_Min([-5, -3, -1, 0, 2, 4]), -5)
