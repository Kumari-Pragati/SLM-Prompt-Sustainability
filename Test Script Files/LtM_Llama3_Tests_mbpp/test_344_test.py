import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(2, 4), 1)
        self.assertEqual(count_Odd_Squares(3, 9), 1)
        self.assertEqual(count_Odd_Squares(4, 16), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(count_Odd_Squares(0, 0), 0)
        self.assertEqual(count_Odd_Squares(1, 0), 0)
        self.assertEqual(count_Odd_Squares(2, 1), 0)
        self.assertEqual(count_Odd_Squares(3, 4), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Odd_Squares('a', 1)
        with self.assertRaises(TypeError):
            count_Odd_Squares(1, 'b')
