import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(Find_Min([-1, -2, -3, -4, -5]), -1)
        self.assertEqual(Find_Min([0, 0, 0]), 0)

    def test_edge_case_empty_list(self):
        self.assertIsNone(Find_Min([]))

    def test_edge_case_single_element(self):
        self.assertEqual(Find_Min([1]), 1)
        self.assertEqual(Find_Min([-1]), -1)

    def test_corner_case_all_same_negative(self):
        self.assertEqual(Find_Min([-1000000, -1000000, -1000000]), -1000000)

    def test_corner_case_all_same_positive(self):
        self.assertEqual(Find_Min([1000000, 1000000, 1000000]), 1000000)
