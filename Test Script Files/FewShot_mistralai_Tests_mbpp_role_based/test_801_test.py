import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):
    def test_three_equal_positive(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_three_equal_duplicates(self):
        self.assertEqual(test_three_equal(1, 1, 2), 0)

    def test_three_equal_negative(self):
        self.assertEqual(test_three_equal(1, 2, 4), 1)

    def test_two_equal(self):
        self.assertEqual(test_three_equal(1, 2), 2)

    def test_one_equal(self):
        self.assertEqual(test_three_equal(1, 2, 3, 4), 3)

    def test_empty_set(self):
        self.assertEqual(test_three_equal(1, 2, 3, 4, 5), 4)
