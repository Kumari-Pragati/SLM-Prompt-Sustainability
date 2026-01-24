import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Squares(2, 5), 14)
        self.assertEqual(count_Squares(3, 3), 10)
        self.assertEqual(count_Squares(1, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(0, 1), 0)
        self.assertEqual(count_Squares(1, 0), 1)

    def test_boundary_cases(self):
        self.assertEqual(count_Squares(2, 2), 5)
        self.assertEqual(count_Squares(10, 10), 385)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Squares("2", 5)
        with self.assertRaises(TypeError):
            count_Squares(2, "5")
        with self.assertRaises(TypeError):
            count_Squares("2", "5")
