import unittest
from mbpp_347_code import count_Squares

class TestCountSquares(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Squares(3, 4), 14)

    def test_swap_m_n(self):
        self.assertEqual(count_Squares(4, 3), 14)

    def test_same_numbers(self):
        self.assertEqual(count_Squares(5, 5), 14)

    def test_negative_numbers(self):
        self.assertEqual(count_Squares(-3, -4), 14)

    def test_zero(self):
        self.assertEqual(count_Squares(0, 4), 0)

    def test_large_numbers(self):
        self.assertEqual(count_Squares(100, 200), 1666650)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_Squares("3", 4)
