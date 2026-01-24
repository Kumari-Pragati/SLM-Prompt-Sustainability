import unittest

from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Odd_Squares(1, 25), 2)

    def test_edge_case(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 0), 0)

    def test_boundary_case(self):
        self.assertEqual(count_Odd_Squares(1, 4), 1)
        self.assertEqual(count_Odd_Squares(1, 9), 1)

    def test_corner_case(self):
        self.assertEqual(count_Odd_Squares(1, 8), 1)
        self.assertEqual(count_Odd_Squares(1, 20), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Odd_Squares('1', 25)
        with self.assertRaises(TypeError):
            count_Odd_Squares(1, '25')
        with self.assertRaises(ValueError):
            count_Odd_Squares(1, -1)
