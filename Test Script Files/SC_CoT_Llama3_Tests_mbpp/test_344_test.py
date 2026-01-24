import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_Odd_Squares(1, 4), 1)
        self.assertEqual(count_Odd_Squares(2, 9), 2)
        self.assertEqual(count_Odd_Squares(3, 16), 2)

    def test_edge_cases(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(2, 4), 1)
        self.assertEqual(count_Odd_Squares(3, 9), 2)

    def test_negative_inputs(self):
        with self.assertRaises(ValueError):
            count_Odd_Squares(-1, 4)
        with self.assertRaises(ValueError):
            count_Odd_Squares(1, -4)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            count_Odd_Squares(1, 4.5)
        with self.assertRaises(TypeError):
            count_Odd_Squares(1.5, 4)

    def test_non_integer_n(self):
        with self.assertRaises(TypeError):
            count_Odd_Squares('a', 4)

    def test_non_integer_m(self):
        with self.assertRaises(TypeError):
            count_Odd_Squares(1, 'b')
