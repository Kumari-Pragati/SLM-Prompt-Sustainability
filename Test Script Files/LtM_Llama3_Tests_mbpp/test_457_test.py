import unittest
from mbpp_457_code import Find_Min

class TestFind_Min(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(Find_Min([1, 2, 3]), 1)

    def test_edge_case_empty(self):
        self.assertRaises( ValueError, Find_Min, [])

    def test_edge_case_single_element(self):
        self.assertEqual(Find_Min([5]), 5)

    def test_edge_case_all_equal(self):
        self.assertEqual(Find_Min([3, 3, 3]), 3)

    def test_edge_case_negative(self):
        self.assertEqual(Find_Min([-5, -2, 0]), -5)

    def test_edge_case_positive(self):
        self.assertEqual(Find_Min([5, 2, 0]), 0)

    def test_edge_case_mixed(self):
        self.assertEqual(Find_Min([-5, 0, 2]), -5)

    def test_edge_case_max(self):
        self.assertEqual(Find_Min([5, 2, 10]), 2)

    def test_edge_case_min(self):
        self.assertEqual(Find_Min([-5, -2, -10]), -10)
