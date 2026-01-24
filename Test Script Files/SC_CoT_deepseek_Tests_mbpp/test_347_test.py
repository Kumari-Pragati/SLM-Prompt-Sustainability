import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Squares(3, 4), 14)

    def test_edge_case(self):
        self.assertEqual(count_Squares(0, 0), 0)

    def test_boundary_case(self):
        self.assertEqual(count_Squares(1, 1), 1)
        self.assertEqual(count_Squares(100, 100), 100 * (100 + 1) * (3 * 1 - 100 + 1) // 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Squares("3", 4)
        with self.assertRaises(TypeError):
            count_Squares(3, "4")
        with self.assertRaises(TypeError):
            count_Squares("3", "4")
        with self.assertRaises(ValueError):
            count_Squares(-3, 4)
        with self.assertRaises(ValueError):
            count_Squares(3, -4)
