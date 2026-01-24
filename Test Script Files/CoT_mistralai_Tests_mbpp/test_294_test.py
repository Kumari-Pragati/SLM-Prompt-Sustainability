import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_negative_integer(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)

    def test_mixed_integer(self):
        self.assertEqual(max_val([1, -2, 3, -4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(max_val([]), None)

    def test_list_with_non_integer(self):
        self.assertEqual(max_val(['a', 1, 'b', 2, 'c']), None)

    def test_list_with_float(self):
        self.assertEqual(max_val([1.1, 2.2, 3.3]), 3.3)

    def test_list_with_zero(self):
        self.assertEqual(max_val([0, 1, 2, 3, 4]), 4)
