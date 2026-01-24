import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Squares(2, 3), 14)

    def test_edge_condition(self):
        self.assertEqual(count_Squares(1, 1), 1)

    def test_boundary_condition(self):
        self.assertEqual(count_Squares(0, 0), 0)
        self.assertEqual(count_Squares(100, 100), 10101)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Squares("2", 3)
        with self.assertRaises(TypeError):
            count_Squares(2, "3")
        with self.assertRaises(TypeError):
            count_Squares("2", "3")
