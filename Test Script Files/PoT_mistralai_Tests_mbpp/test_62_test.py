import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(smallest_num([0, 0, 0]), 0)

    def test_edge_case_empty_list(self):
        self.assertIsNone(smallest_num([]))

    def test_edge_case_single_element(self):
        self.assertEqual(smallest_num([1]), 1)
        self.assertEqual(smallest_num([-1]), -1)
        self.assertEqual(smallest_num([0]), 0)

    def test_corner_case_negative_zero(self):
        self.assertEqual(smallest_num([0, -0]), 0)
