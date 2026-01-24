import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(square_Sum(5), 140)

    def test_boundary_conditions(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(1), 2)

    def test_large_number(self):
        self.assertEqual(square_Sum(100), 832030)

    def test_negative_number(self):
        self.assertEqual(square_Sum(-5), 140)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            square_Sum('a')
