import unittest
from mbpp_488_code import sqrt, pow
from decimal import Decimal

def area_pentagon(a):
  area = (sqrt(5 * (5 + 2 * sqrt(5))) * pow(a, 2)) / 4.0
  return area

class TestAreaPentagon(unittest.TestCase):

    def test_area_pentagon_with_valid_input(self):
        self.assertAlmostEqual(area_pentagon(3), Decimal('9.464101635'), places=6)
        self.assertAlmostEqual(area_pentagon(4), Decimal('18.94427191'), places=6)
        self.assertAlmostEqual(area_pentagon(5), Decimal('28.42431310'), places=6)

    def test_area_pentagon_with_zero(self):
        self.assertAlmostEqual(area_pentagon(0), 0.0, places=6)

    def test_area_pentagon_with_negative_input(self):
        self.assertRaises(ValueError, area_pentagon, -1)
