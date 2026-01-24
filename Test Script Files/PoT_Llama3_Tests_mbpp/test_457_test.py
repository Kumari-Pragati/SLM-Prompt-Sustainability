import unittest
from mbpp_457_code import Find_Min

class TestFind_Min(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(Find_Min([]), None)

    def test_edge_case_single_element_list(self):
        self.assertEqual(Find_Min([10]), 10)

    def test_edge_case_negative_numbers(self):
        self.assertEqual(Find_Min([-5, -3, -1]), -5)

    def test_edge_case_positive_numbers(self):
        self.assertEqual(Find_Min([5, 3, 1]), 1)

    def test_edge_case_mixed_numbers(self):
        self.assertEqual(Find_Min([5, -3, 1, 0]), -3)

    def test_edge_case_duplicates(self):
        self.assertEqual(Find_Min([5, 5, 3, 1]), 1)
