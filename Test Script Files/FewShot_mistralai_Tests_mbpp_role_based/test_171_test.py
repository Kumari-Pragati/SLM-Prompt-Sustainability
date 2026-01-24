import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(perimeter_pentagon(3), 15)

    def test_zero(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_negative_number(self):
        self.assertRaises(ValueError, perimeter_pentagon, -1)

    def test_non_numeric_input(self):
        self.assertRaises(TypeError, perimeter_pentagon, 'invalid')
