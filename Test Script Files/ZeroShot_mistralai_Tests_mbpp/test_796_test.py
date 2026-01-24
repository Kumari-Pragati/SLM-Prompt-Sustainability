import unittest
from mbpp_796_code import Dict

from 796_code import return_sum

class TestReturnSum(unittest.TestCase):

    def test_empty_dict(self):
        self.assertEqual(return_sum({}), 0)

    def test_single_key_dict(self):
        self.assertEqual(return_sum({"key": 1}), 1)

    def test_multiple_key_dict(self):
        self.assertEqual(return_sum({"key1": 1, "key2": 2, "key3": 3}), 6)

    def test_negative_values(self):
        self.assertEqual(return_sum({"key1": -1, "key2": 2, "key3": -3}), 0)

    def test_mixed_values(self):
        self.assertEqual(return_sum({"key1": 1, "key2": -2, "key3": 3}), 2)
