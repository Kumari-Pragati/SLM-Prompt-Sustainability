import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(sum_Square(5))

    def test_edge_case(self):
        self.assertFalse(sum_Square(1))

    def test_boundary_case(self):
        self.assertFalse(sum_Square(0))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_Square('a')
