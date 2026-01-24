import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(perimeter_pentagon(5), 25)

    def test_zero_length(self):
        self.assertAlmostEqual(perimeter_pentagon(0), 0)

    def test_negative_length(self):
        with self.assertRaises(ValueError):
            perimeter_pentagon(-5)

    def test_large_number(self):
        self.assertAlmostEqual(perimeter_pentagon(10000), 50000)

    def test_float_length(self):
        self.assertAlmostEqual(perimeter_pentagon(3.5), 17.5)
