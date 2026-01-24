import unittest
from mbpp_76_code import count_Squares

class TestCountSquares(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_Squares(2, 5), 14)

    def test_edge_condition(self):
        self.assertEqual(count_Squares(0, 0), 0)

    def test_boundary_condition(self):
        self.assertEqual(count_Squares(1, 1), 1)

    def test_m_greater_than_n(self):
        self.assertEqual(count_Squares(5, 2), 14)

    def test_negative_numbers(self):
        self.assertEqual(count_Squares(-2, -5), 14)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Squares("2", 5)
