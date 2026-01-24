import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):

    def test_perimeter_pentagon_positive(self):
        # Typical case: valid positive input
        a = 5
        expected = 25
        self.assertEqual(perimeter_pentagon(a), expected)

    def test_perimeter_pentagon_zero(self):
        # Edge case: zero input
        a = 0
        with self.assertRaises(ValueError):
            perimeter_pentagon(a)

    def test_perimeter_pentagon_negative(self):
        # Edge case: negative input
        a = -3
        with self.assertRaises(ValueError):
            perimeter_pentagon(a)

    def test_perimeter_pentagon_float(self):
        # Edge case: float input
        a = 3.14
        expected = round(5 * a, 2)  # Round to 2 decimal places
        self.assertEqual(perimeter_pentagon(a), expected)
