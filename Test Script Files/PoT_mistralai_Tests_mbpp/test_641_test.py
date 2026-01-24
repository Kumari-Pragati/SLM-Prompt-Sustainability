import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(is_nonagonal(3), 6)
        self.assertEqual(is_nonagonal(5), 25)
        self.assertEqual(is_nonagonal(7), 77)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(is_nonagonal(1), 0)
        self.assertEqual(is_nonagonal(2), 2)
        self.assertEqual(is_nonagonal(4), 20)
        self.assertEqual(is_nonagonal(6), 42)
        self.assertEqual(is_nonagonal(8), 84)
        self.assertEqual(is_nonagonal(9), 108)
