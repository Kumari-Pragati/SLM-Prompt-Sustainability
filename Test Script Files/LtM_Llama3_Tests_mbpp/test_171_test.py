import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):
    def test_perimeter_pentagon_typical(self):
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_perimeter_pentagon_zero(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_perimeter_pentagon_negative(self):
        self.assertEqual(perimeter_pentagon(-5), 0)

    def test_perimeter_pentagon_non_integer(self):
        self.assertEqual(perimeter_pentagon(5.5), 27.5)

    def test_perimeter_pentagon_invalid_input(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon('a')
