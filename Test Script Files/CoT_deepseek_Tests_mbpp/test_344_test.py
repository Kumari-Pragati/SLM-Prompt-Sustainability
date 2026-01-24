import unittest
from mbpp_344_code import count_Odd_Squares

class TestCountOddSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Odd_Squares(1, 25), 2)

    def test_boundary_conditions(self):
        self.assertEqual(count_Odd_Squares(1, 1), 0)
        self.assertEqual(count_Odd_Squares(1, 0), 0)
        self.assertEqual(count_Odd_Squares(1, -1), 0)

    def test_edge_cases(self):
        self.assertEqual(count_Odd_Squares(1, 2), 1)
        self.assertEqual(count_Odd_Squares(1, 3), 1)
        self.assertEqual(count_Odd_Squares(1, 4), 1)
        self.assertEqual(count_Odd_Squares(1, 5), 2)
        self.assertEqual(count_Odd_Squares(1, 6), 2)
        self.assertEqual(count_Odd_Squares(1, 7), 2)
        self.assertEqual(count_Odd_Squares(1, 8), 2)
        self.assertEqual(count_Odd_Squares(1, 9), 2)
        self.assertEqual(count_Odd_Squares(1, 10), 2)
        self.assertEqual(count_Odd_Squares(1, 11), 2)
        self.assertEqual(count_Odd_Squares(1, 12), 2)
        self.assertEqual(count_Odd_Squares(1, 13), 2)
        self.assertEqual(count_Odd_Squares(1, 14), 2)
        self.assertEqual(count_Odd_Squares(1, 15), 2)
        self.assertEqual(count_Odd_Squares(1, 16), 2)
        self.assertEqual(count_Odd_Squares(1, 17), 2)
        self.assertEqual(count_Odd_Squares(1, 18), 2)
        self.assertEqual(count_Odd_Squares(1, 19), 2)
        self.assertEqual(count_Odd_Squares(1, 20), 2)
        self.assertEqual(count_Odd_Squares(1, 21), 2)
        self.assertEqual(count_Odd_Squares(1, 22), 2)
        self.assertEqual(count_Odd_Squares(1, 23), 2)
        self.assertEqual(count_Odd_Squares(1, 24), 2)
        self.assertEqual(count_Odd_Squares(1, 25), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Odd_Squares('1', 25)
        with self.assertRaises(TypeError):
            count_Odd_Squares(1, '25')
        with self.assertRaises(TypeError):
            count_Odd_Squares('1', '25')
