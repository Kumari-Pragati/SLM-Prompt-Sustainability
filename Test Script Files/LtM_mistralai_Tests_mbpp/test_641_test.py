import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(is_nonagonal(1), 0)
        self.assertEqual(is_nonagonal(2), 2)
        self.assertEqual(is_nonagonal(3), 6)
        self.assertEqual(is_nonagonal(4), 12)
        self.assertEqual(is_nonagonal(5), 20)

    def test_edge_cases(self):
        self.assertEqual(is_nonagonal(0), -1)
        self.assertEqual(is_nonagonal(10), 165)

    def test_negative_and_floats(self):
        self.assertEqual(is_nonagonal(-1), -1)
        self.assertAlmostEqual(is_nonagonal(2.5), 5.5)
