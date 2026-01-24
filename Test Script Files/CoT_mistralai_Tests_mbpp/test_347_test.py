import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_Squares(3, 4), 14)
        self.assertEqual(count_Squares(4, 5), 21)
        self.assertEqual(count_Squares(5, 6), 30)

    def test_edge_cases(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 2), 3)
        self.assertEqual(count_Squares(3, 3), 9)

    def test_boundary_conditions(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(0, 1), 1)
        self.assertEqual(count_Squares(1, 0), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, count_Squares, 'a', 'b')
        self.assertRaises(TypeError, count_Squares, 0.5, 1)
        self.assertRaises(TypeError, count_Squares, 1, 0.5)
