import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5]), 1)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(smallest_num([0]), 0)

    def test_edge_conditions(self):
        self.assertEqual(smallest_num([]), None)
        self.assertEqual(smallest_num([1]), 1)

    def test_complex_cases(self):
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, 0]), 0)
        self.assertEqual(smallest_num([-1, -2, -3, -4, -5, 0]), -5)
        self.assertEqual(smallest_num([1, 2, 3, 4, 5, -10]), -10)
