import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_Squares(5, 7), 55)

    def test_edge_cases(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 2), 6)
        self.assertEqual(count_Squares(3, 3), 14)
        self.assertEqual(count_Squares(4, 4), 30)

    def test_boundary_cases(self):
        self.assertEqual(count_Squares(5, 5), 30)
        self.assertEqual(count_Squares(6, 6), 36)
        self.assertEqual(count_Squares(7, 7), 44)
        self.assertEqual(count_Squares(8, 8), 56)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Squares('a', 5)
        with self.assertRaises(TypeError):
            count_Squares(5, 'b')
