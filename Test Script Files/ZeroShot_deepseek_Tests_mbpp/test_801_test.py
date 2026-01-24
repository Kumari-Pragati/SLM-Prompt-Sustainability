import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):

    def test_all_equal(self):
        self.assertEqual(test_three_equal(1, 1, 1), 0)

    def test_two_equal(self):
        self.assertEqual(test_three_equal(1, 1, 2), 1)

    def test_all_different(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)
