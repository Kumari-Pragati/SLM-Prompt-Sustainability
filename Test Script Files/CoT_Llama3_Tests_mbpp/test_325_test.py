import unittest
from mbpp_325_code import get_Min_Squares

class TestGetMinSquares(unittest.TestCase):
    def test_get_Min_Squares_typical(self):
        self.assertEqual(get_Min_Squares(12), 3)

    def test_get_Min_Squares_edge(self):
        self.assertEqual(get_Min_Squares(3), 3)
        self.assertEqual(get_Min_Squares(2), 1)
        self.assertEqual(get_Min_Squares(1), 1)

    def test_get_Min_Squares_invalid(self):
        with self.assertRaises(TypeError):
            get_Min_Squares('a')

    def test_get_Min_Squares_boundary(self):
        self.assertEqual(get_Min_Squares(4), 2)
        self.assertEqual(get_Min_Squares(5), 1)

    def test_get_Min_Squares_zero(self):
        self.assertEqual(get_Min_Squares(0), 0)
