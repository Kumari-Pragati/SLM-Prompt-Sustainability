import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):
    def test_positive_integers(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_negative_integers(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)

    def test_mixed_integers(self):
        self.assertEqual(max_val([1, -2, 3, -4, 5]), 5)

    def test_empty_list(self):
        self.assertIsNone(max_val([]))

    def test_list_with_non_integer(self):
        self.assertIsNone(max_val([1, 'a', 3]))
