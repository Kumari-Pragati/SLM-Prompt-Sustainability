import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):
    def test_even_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4], 4, 1), "EVEN")

    def test_odd_sum(self):
        self.assertEqual(check_last([1, 2, 3, 5], 4, 1), "ODD")

    def test_zero_sum(self):
        self.assertEqual(check_last([0, 0, 0, 0], 4, 1), "EVEN")

    def test_single_element(self):
        self.assertEqual(check_last([1], 1, 1), "EVEN")

    def test_empty_array(self):
        with self.assertRaises(IndexError):
            check_last([], 0, 1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            check_last([1, 2, 3, 4], "four", 1)

    def test_non_integer_p(self):
        with self.assertRaises(TypeError):
            check_last([1, 2, 3, 4], 4, "one")
