import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):
    def test_three_equal_typical(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)
        self.assertEqual(test_three_equal(1, 1, 1), 0)
        self.assertEqual(test_three_equal(0, 0, 0), 0)

    def test_three_equal_edge(self):
        self.assertEqual(test_three_equal(1, 2, 4), 1)
        self.assertEqual(test_three_equal(1, 1, 4), 1)
        self.assertEqual(test_three_equal(0, 0, 1), 1)
        self.assertEqual(test_three_equal(1, 0, 0), 1)
        self.assertEqual(test_three_equal(0, 1, 0), 1)
        self.assertEqual(test_three_equal(0, 0, 1), 1)

    def test_three_equal_invalid(self):
        self.assertRaises(TypeError, test_three_equal, 'a', 'b', 'c')
        self.assertRaises(TypeError, test_three_equal, 1, 'b', 3)
        self.assertRaises(TypeError, test_three_equal, 1, 2, 'c')
