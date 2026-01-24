import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):

    def test_all_different_numbers(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_two_equal_numbers(self):
        self.assertEqual(test_three_equal(1, 1, 2), 2)

    def test_all_equal_numbers(self):
        self.assertEqual(test_three_equal(1, 1, 1), 3)

    def test_negative_numbers(self):
        self.assertEqual(test_three_equal(-1, -2, -3), 0)

    def test_zero(self):
        self.assertEqual(test_three_equal(0, 0, 0), 3)

    def test_large_numbers(self):
        self.assertEqual(test_three_equal(1000, 1000, 1000), 3)

    def test_float_numbers(self):
        self.assertEqual(test_three_equal(1.1, 1.2, 1.3), 0)

    def test_string_numbers(self):
        with self.assertRaises(TypeError):
            test_three_equal("1", "2", "3")

    def test_none_numbers(self):
        with self.assertRaises(TypeError):
            test_three_equal(None, None, None)
