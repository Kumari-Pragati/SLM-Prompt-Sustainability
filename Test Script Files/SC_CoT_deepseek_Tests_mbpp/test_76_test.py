import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_typical_case(self):
        self.assertAlmostEqual(count_Squares(3, 5), 14.0)

    def test_edge_cases(self):
        self.assertAlmostEqual(count_Squares(0, 0), 0.0)
        self.assertAlmostEqual(count_Squares(1, 1), 1.0)
        self.assertAlmostEqual(count_Squares(2, 2), 5.0)

    def test_boundary_conditions(self):
        self.assertAlmostEqual(count_Squares(1, 10), 30.5)
        self.assertAlmostEqual(count_Squares(10, 1), 30.5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_Squares("3", 5)
        with self.assertRaises(TypeError):
            count_Squares(3, "5")
        with self.assertRaises(TypeError):
            count_Squares("3", "5")
        with self.assertRaises(ValueError):
            count_Squares(-3, 5)
        with self.assertRaises(ValueError):
            count_Squares(3, -5)
