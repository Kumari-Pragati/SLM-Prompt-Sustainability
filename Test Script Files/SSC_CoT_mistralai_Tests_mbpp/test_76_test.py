import unittest
from mbpp_76_code import MagicMock

from76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(count_Squares(3, 5), 14)
        self.assertEqual(count_Squares(5, 5), 6)
        self.assertEqual(count_Squares(10, 20), 385)

    def test_edge_cases(self):
        self.assertEqual(count_Squares(0, 5), 6)
        self.assertEqual(count_Squares(5, 0), 0)
        self.assertEqual(count_Squares(0, 0), 0)

    def test_boundary_cases(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(2, 2), 3)
        self.assertEqual(count_Squares(100, 100), 338350)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Squares('a', 'b')
        with self.assertRaises(TypeError):
            count_Squares(1.5, 2)
        with self.assertRaises(TypeError):
            count_Squares(MagicMock(), 2)
