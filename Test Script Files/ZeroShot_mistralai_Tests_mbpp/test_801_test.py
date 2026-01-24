import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):

    def test_three_equal_three_same(self):
        self.assertEqual(test_three_equal(1, 1, 1), 0)
        self.assertEqual(test_three_equal('a', 'a', 'a'), 0)
        self.assertEqual(test_three_equal(1.0, 1.0, 1.0), 0)

    def test_three_equal_two_same_one_different(self):
        self.assertEqual(test_three_equal(1, 1, 2), 1)
        self.assertEqual(test_three_equal('a', 'a', 'b'), 1)
        self.assertEqual(test_three_equal(1.0, 1.0, 2.0), 1)

    def test_three_equal_three_different(self):
        self.assertEqual(test_three_equal(1, 2, 3), 3)
        self.assertEqual(test_three_equal('a', 'b', 'c'), 3)
        self.assertEqual(test_three_equal(1.0, 2.0, 3.0), 3)
