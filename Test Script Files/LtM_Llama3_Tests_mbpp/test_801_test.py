import unittest
from mbpp_801_code import test_three_equal

class TestTestThreeEqual(unittest.TestCase):
    def test_three_equal_typical(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)

    def test_three_equal_empty(self):
        self.assertEqual(test_three_equal(1, 2, 0), 2)

    def test_three_equal_single(self):
        self.assertEqual(test_three_equal(1, 2, 1), 1)

    def test_three_equal_duplicates(self):
        self.assertEqual(test_three_equal(1, 1, 1), 1)

    def test_three_equal_negative(self):
        self.assertEqual(test_three_equal(-1, -2, -3), 0)

    def test_three_equal_mixed(self):
        self.assertEqual(test_three_equal(1, -2, 3), 0)
