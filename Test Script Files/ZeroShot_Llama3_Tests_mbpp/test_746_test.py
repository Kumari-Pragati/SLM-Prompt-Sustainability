import unittest
from mbpp_746_code import sector_area

class TestSectorArea(unittest.TestCase):

    def test_sector_area(self):
        self.assertEqual(sector_area(5, 90), 78.57142857142857)
        self.assertEqual(sector_area(10, 180), 157.14285714285714)
        self.assertEqual(sector_area(15, 270), 235.71428571428572)
        self.assertEqual(sector_area(20, 360), None)
        self.assertEqual(sector_area(-5, 90), None)
        self.assertEqual(sector_area(5, -90), None)
        self.assertEqual(sector_area(5, 0), None)
        self.assertEqual(sector_area(5, 360), None)

    def test_sector_area_invalid_input(self):
        with self.assertRaises(TypeError):
            sector_area('a', 90)
        with self.assertRaises(TypeError):
            sector_area(5, 'b')
        with self.assertRaises(TypeError):
            sector_area(None, 90)
        with self.assertRaises(TypeError):
            sector_area(5, None)
