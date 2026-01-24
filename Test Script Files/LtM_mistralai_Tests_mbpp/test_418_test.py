import unittest
from mbpp_418_code import Find_Max

class TestFindMax(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(Find_Max([1, 2, 3]), 3)
        self.assertEqual(Find_Max([-1, -2, -3]), -3)
        self.assertEqual(Find_Max([0, 0, 0]), 0)

    def test_edge_input(self):
        self.assertEqual(Find_Max([]), None)
        self.assertEqual(Find_Max([999999]), 999999)
        self.assertEqual(Find_Max([-999999]), -999999)

    def test_complex_input(self):
        self.assertEqual(Find_Max([1, -1, 1, -1]), 1)
        self.assertEqual(Find_Max([-1, -2, -3, -4]), -4)
        self.assertEqual(Find_Max([0, 1, 2, 3]), 3)
        self.assertEqual(Find_Max([-1, -2, -3, -4]), -4)
        self.assertEqual(Find_Max([-1, 0, 1, 2]), 2)
