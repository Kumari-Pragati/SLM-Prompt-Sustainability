import unittest
from mbpp_112_code import perimeter

class TestPerimeterFunction(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertAlmostEqual(perimeter(10, 5), 30)
        
    def test_zero_height(self):
        self.assertAlmostEqual(perimeter(10, 0), 20)
        
    def test_zero_diameter(self):
        self.assertAlmostEqual(perimeter(0, 5), 10)
        
    def test_negative_values(self):
        with self.assertRaises(Exception):
            perimeter(-10, 5)
            
    def test_zero_values(self):
        self.assertAlmostEqual(perimeter(0, 0), 0)
