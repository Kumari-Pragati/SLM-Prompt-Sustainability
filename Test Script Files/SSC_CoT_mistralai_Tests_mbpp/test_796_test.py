import unittest
from mbpp_796_code import MagicMock

from796_code import return_sum

class TestReturnSum(unittest.TestCase):

    def test_normal_input(self):
        data = {'a': 1, 'b': 2, 'c': 3}
        result = return_sum(data)
        self.assertEqual(result, 6)

    def test_empty_input(self):
        data = {}
        result = return_sum(data)
        self.assertEqual(result, 0)

    def test_single_value_input(self):
        data = {'key': 5}
        result = return_sum(data)
        self.assertEqual(result, 5)

    def test_negative_values(self):
        data = {'a': -1, 'b': 2, 'c': -3}
        result = return_sum(data)
        self.assertEqual(result, -2)

    def test_large_values(self):
        data = {'a': 1000000, 'b': 2, 'c': 3}
        result = return_sum(data)
        self.assertEqual(result, 1000002)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            return_sum(MagicMock())
