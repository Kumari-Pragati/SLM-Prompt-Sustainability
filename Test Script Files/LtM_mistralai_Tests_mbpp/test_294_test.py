import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):

    def test_simple_int_list(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(max_val([]), None)

    def test_mixed_list(self):
        self.assertEqual(max_val([1, 'a', 3, 'b', 5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)

    def test_large_numbers(self):
        self.assertEqual(max_val([1000000001, 1000000002, 1000000003]), 1000000003)

    def test_single_int(self):
        self.assertEqual(max_val([1]), 1)
