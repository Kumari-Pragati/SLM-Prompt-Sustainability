import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):
    def test_three_equal_typical(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)
        self.assertEqual(test_three_equal(1, 1, 2), 0)
        self.assertEqual(test_three_equal(2, 2, 2), 0)

    def test_three_equal_edge(self):
        self.assertEqual(test_three_equal(1, 1, 1), 0)
        self.assertEqual(test_three_equal(1, 1, 4), 1)
        self.assertEqual(test_three_equal(1, 4, 4), 1)
        self.assertEqual(test_three_equal(4, 4, 4), 0)

    def test_three_equal_corner(self):
        self.assertEqual(test_three_equal(1, 1, 1.0), 1)
        self.assertEqual(test_three_equal('1', '1', '2'), 1)
        self.assertEqual(test_three_equal(None, 1, 2), 3)
        self.assertEqual(test_three_equal(1, None, 2), 3)
        self.assertEqual(test_three_equal(1, 2, None), 3)
