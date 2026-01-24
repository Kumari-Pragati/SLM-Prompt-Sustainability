import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(return_sum({1: 1, 2: 2, 3: 3}), 6)
        self.assertEqual(return_sum({0: 0, 1: 1, 2: 2}), 3)
        self.assertEqual(return_sum({-1: -1, 0: 0, 1: 1}), 0)

    def test_edge_cases(self):
        self.assertEqual(return_sum({}), 0)
        self.assertEqual(return_sum({1: float('inf')}), float('inf'))
        self.assertEqual(return_sum({float('-inf'): 1}), -1)

    def test_complex(self):
        self.assertEqual(return_sum({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}), 15)
        self.assertEqual(return_sum({1: -1, 2: -2, 3: -3, 4: -4, 5: -5}), -15)
        self.assertEqual(return_sum({1: 1, 2: -2, 3: 3, 4: -4, 5: 5}), 5)
