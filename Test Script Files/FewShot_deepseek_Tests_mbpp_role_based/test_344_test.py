import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Odd_Squares(1, 25), 2)

    def test_boundary_conditions(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 0), 0)
        self.assertEqual(count_Odd_Squares(1, -1), 0)

    def test_edge_conditions(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 2), 1)
        self.assertEqual(count_Odd_squares(1, 3), 1)
        self.assertEqual(count_Odd_squares(1, 4), 1)
        self.assertEqual(count_Odd_squares(1, 5), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Odd_Squares("1", 2)
        with self.assertRaises(TypeError):
            count_Odd_Squares(1, "2")
        with self.assertRaises(TypeError):
            count_Odd_Squares("1", "2")
