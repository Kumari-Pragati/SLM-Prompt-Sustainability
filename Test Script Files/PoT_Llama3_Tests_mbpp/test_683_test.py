import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):
    def test_typical_cases(self):
        self.assertTrue(sum_Square(5))
        self.assertTrue(sum_Square(13))
        self.assertFalse(sum_Square(14))

    def test_edge_cases(self):
        self.assertFalse(sum_Square(0))
        self.assertFalse(sum_Square(1))
        self.assertTrue(sum_Square(4))

    def test_boundary_cases(self):
        self.assertFalse(sum_Square(2))
        self.assertFalse(sum_Square(3))
        self.assertTrue(sum_Square(10))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_Square('a')
