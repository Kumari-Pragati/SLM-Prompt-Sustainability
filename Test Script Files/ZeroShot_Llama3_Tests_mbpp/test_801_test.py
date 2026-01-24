import unittest
from mbpp_801_code import test_three_equal

class TestTestThreeEqual(unittest.TestCase):

    def test_three_equal_true(self):
        self.assertEqual(test_three_equal(1,2,3), 0)

    def test_three_equal_false(self):
        self.assertEqual(test_three_equal(1,2,1), 2)

    def test_three_equal_zero(self):
        self.assertEqual(test_three_equal(1,1,1), 0)

    def test_three_equal_one(self):
        self.assertEqual(test_three_equal(1,2,3), 0)

    def test_three_equal_two(self):
        self.assertEqual(test_three_equal(1,1,2), 1)

    def test_three_equal_three(self):
        self.assertEqual(test_three_equal(1,1,1), 0)

    def test_three_equal_four(self):
        self.assertEqual(test_three_equal(1,2,3), 0)

    def test_three_equal_five(self):
        self.assertEqual(test_three_equal(1,1,1), 0)
