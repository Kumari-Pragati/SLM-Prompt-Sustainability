import unittest
from mbpp_287_code import square_Sum

class TestSquareSum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(square_Sum(1), 1)
        self.assertEqual(square_Sum(2), 5)
        self.assertEqual(square_Sum(3), 14)
        self.assertEqual(square_Sum(4), 30)

    def test_boundary_conditions(self):
        self.assertEqual(square_Sum(0), 0)
        self.assertEqual(square_Sum(100), 338350)

    def test_negative_numbers(self):
        self.assertEqual(square_Sum(-1), 1)
        self.assertEqual(square_Sum(-2), -1)
        self.assertEqual(square_Sum(-3), -4)

    def test_large_numbers(self):
        self.assertEqual(square_Sum(1000), 333833500)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            square_Sum('a')
        with self.assertRaises(TypeError):
            square_Sum(None)
        with self.assertRaises(TypeError):
            square_Sum([])
