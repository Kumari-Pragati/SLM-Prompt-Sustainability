import unittest
from mbpp_796_code import return_sum

class TestReturnSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(return_sum({'a': 1, 'b': 2, 'c': 3}), 6)

    def test_edge_case_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_edge_case_single_key(self):
        self.assertEqual(return_sum({'a': 1}), 1)

    def test_edge_case_negative_values(self):
        self.assertEqual(return_sum({'a': -1, 'b': 2}), 1)

    def test_corner_case_keys_with_zero(self):
        self.assertEqual(return_sum({'a': 0, 'b': 1}), 1)
