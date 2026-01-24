import unittest
from mbpp_426_code import filter_oddnumbers

class TestFilterOddNumbers(unittest.TestCase):

    def test_filter_oddnumbers_normal(self):
        self.assertListEqual(filter_oddnumbers([1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertListEqual(filter_oddnumbers([-1, 0, -3, 4, -5]), [-1, -3, -5])

    def test_filter_oddnumbers_edge_cases(self):
        self.assertListEqual(filter_oddnumbers([]), [])
        self.assertListEqual(filter_oddnumbers([0]), [])
        self.assertListEqual(filter_oddnumbers([2]), [])

    def test_filter_oddnumbers_boundary_cases(self):
        self.assertListEqual(filter_oddnumbers([-1, 1]), [-1])
        self.assertListEqual(filter_oddnumbers([1, 2, 3, 2]), [1, 3])
