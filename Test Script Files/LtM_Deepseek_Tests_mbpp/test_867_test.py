import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(min_Num([1, 2, 3], 3), 2)
        self.assertEqual(min_Num([2, 4, 6], 3), 2)
        self.assertEqual(min_Num([1, 3, 5], 3), 1)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(min_Num([], 0), 2)
        self.assertEqual(min_Num([1], 1), 1)
        self.assertEqual(min_Num([2], 1), 2)
        self.assertEqual(min_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 2)

    def test_more_complex_cases(self):
        self.assertEqual(min_Num([1, 3, 5, 7, 9], 5), 1)
        self.assertEqual(min_Num([2, 4, 6, 8, 10], 5), 2)
        self.assertEqual(min_Num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 11), 2)
