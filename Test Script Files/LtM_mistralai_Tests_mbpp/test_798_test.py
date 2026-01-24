import unittest
from mbpp_798_code import _sum

class TestSumFunction(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(_sum([1, 2, 3]), 6)

    def test_empty_input(self):
        self.assertEqual(_sum([]), 0)

    def test_single_input(self):
        self.assertEqual(_sum([4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(_sum([1, -2, 3]), 2)

    def test_large_numbers(self):
        self.assertEqual(_sum([1000000001, 1000000002, 1000000003]), 3000000006)

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            _sum([1, 2, '3', 4])
