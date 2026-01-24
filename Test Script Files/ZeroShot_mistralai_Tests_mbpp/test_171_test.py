import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):

    def test_perimeter_pentagon_positive(self):
        self.assertEqual(perimeter_pentagon(3), 15)
        self.assertEqual(perimeter_pentagon(4), 20)
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_perimeter_pentagon_zero(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_perimeter_pentagon_negative(self):
        self.assertEqual(perimeter_pentagon(-1), math.nan)
