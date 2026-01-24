import unittest
from mbpp_697_code import count_even

class TestCountEven(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(count_even([]), 0)

    def test_single_even(self):
        self.assertEqual(count_even([4]), 1)

    def test_single_odd(self):
        self.assertEqual(count_even([3]), 0)

    def test_multiple_even(self):
        self.assertEqual(count_even([2, 4, 6]), 3)

    def test_multiple_odd(self):
        self.assertEqual(count_even([1, 3, 5]), 0)

    def test_mixed(self):
        self.assertEqual(count_even([2, 4, 3, 6, 1]), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_even([-2, -4, 3, 6, 1]), 3)

    def test_non_integer(self):
        with self.assertRaises(TypeError):
            count_even([2, 4, 'a', 6, 1])
