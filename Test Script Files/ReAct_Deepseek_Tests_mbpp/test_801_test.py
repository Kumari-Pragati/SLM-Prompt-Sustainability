import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):

    def test_all_equal(self):
        self.assertEqual(test_three_equal(1, 1, 1), 0)

    def test_two_equal(self):
        self.assertEqual(test_three_equal(1, 1, 2), 2)

    def test_all_different(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_negative_numbers(self):
        self.assertEqual(test_three_equal(-1, -2, -3), 0)

    def test_zero(self):
        self.assertEqual(test_three_equal(0, 0, 0), 2)

    def test_large_numbers(self):
        self.assertEqual(test_three_equal(1000, 1000, 1000), 0)

    def test_large_range_numbers(self):
        self.assertEqual(test_three_equal(1, 1000, 2000), 2)
