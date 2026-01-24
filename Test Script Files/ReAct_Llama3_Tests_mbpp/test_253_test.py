import unittest
from mbpp_253_code import count_integer

class TestCountInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_integer([]), 0)

    def test_single_integer(self):
        self.assertEqual(count_integer([1]), 1)

    def test_multiple_integers(self):
        self.assertEqual(count_integer([1, 2, 3]), 3)

    def test_non_integer_values(self):
        self.assertEqual(count_integer([1, 2, 'a', 4]), 3)

    def test_mixed_types(self):
        self.assertEqual(count_integer([1, 2, 3, 'a', 4, 5.5]), 4)

    def test_negative_integer(self):
        self.assertEqual(count_integer([-1, 2, 3]), 2)

    def test_zero(self):
        self.assertEqual(count_integer([0, 1, 2]), 2)

    def test_large_list(self):
        self.assertEqual(count_integer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
