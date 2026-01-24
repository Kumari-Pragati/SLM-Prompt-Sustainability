import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):
    def test_perimeter_pentagon_positive(self):
        self.assertEqual(perimeter_pentagon(3), 15)
        self.assertEqual(perimeter_pentagon(5), 25)
        self.assertEqual(perimeter_pentagon(10), 50)

    def test_perimeter_pentagon_zero(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_perimeter_pentagon_negative(self):
        self.assertEqual(perimeter_pentagon(-3), 0)

    def test_perimeter_pentagon_float(self):
        self.assertAlmostEqual(perimeter_pentagon(3.5), 17.5)
