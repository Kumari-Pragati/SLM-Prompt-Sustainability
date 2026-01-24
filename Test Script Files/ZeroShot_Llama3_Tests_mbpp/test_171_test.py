import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):

    def test_perimeter_pentagon_positive(self):
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_perimeter_pentagon_negative(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon(-5)

    def test_perimeter_pentagon_zero(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon(0)

    def test_perimeter_pentagon_non_numeric(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon('five')
