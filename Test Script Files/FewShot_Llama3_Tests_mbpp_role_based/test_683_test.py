import unittest
from mbpp_683_code import sum_Square

class TestSumSquare(unittest.TestCase):
    def test_true_sum_square(self):
        self.assertTrue(sum_Square(5))

    def test_false_sum_square(self):
        self.assertFalse(sum_Square(10))

    def test_edge_case_sum_square(self):
        self.assertTrue(sum_Square(4))

    def test_edge_case_sum_square_false(self):
        self.assertFalse(sum_Square(3))

    def test_invalid_input_sum_square(self):
        with self.assertRaises(TypeError):
            sum_Square('a')
