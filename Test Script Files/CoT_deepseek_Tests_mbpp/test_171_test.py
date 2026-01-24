import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):

    def test_positive_side_length(self):
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_zero_side_length(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_negative_side_length(self):
        with self.assertRaises(Exception):
            perimeter_pentagon(-5)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon('five')
