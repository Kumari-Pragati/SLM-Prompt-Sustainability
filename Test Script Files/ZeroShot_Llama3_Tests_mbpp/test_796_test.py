import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):

    def test_return_sum(self):
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3}), 6)
        self.assertEqual(return_sum({'x': 4, 'y': 5}), 9)
        self.assertEqual(return_sum({}), 0)
        self.assertEqual(return_sum({'z': -1, 'w': 2}), 1)
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3, 'd': 4}), 10)

    def test_return_sum_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_return_sum_negative_numbers(self):
        self.assertEqual(return_sum({'a': -1, 'b': 2}), 1)

    def test_return_sum_multiple_negative_numbers(self):
        self.assertEqual(return_sum({'a': -1, 'b': -2, 'c': -3}), -6)
