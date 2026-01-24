import unittest
from mbpp_905_code import patch

class TestSumOfSquare(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(sum_of_square(1), 1)
        self.assertEqual(sum_of_square(5), 58)

    def test_edge_cases(self):
        self.assertEqual(sum_of_square(0), 0)
        self.assertEqual(sum_of_square(100), 278793027200)

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            sum_of_square(-1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            sum_of_square(1.5)

    def test_zero_factorial(self):
        with patch('905_code.factorial') as mock_factorial:
            mock_factorial.return_value = 0
            with self.assertRaises(ZeroDivisionError):
                sum_of_square(0)
