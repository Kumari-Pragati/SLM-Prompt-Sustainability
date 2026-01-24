import unittest
from mbpp_112_code import perimeter

class TestPerimeter(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertAlmostEqual(perimeter(10, 5), 30)
        
    def test_edge_cases(self):
        self.assertAlmostEqual(perimeter(0, 0), 0)
        self.assertAlmostEqual(perimeter(10000000, 0), 20000000)
        self.assertAlmostEqual(perimeter(0, 10000000), 20000000)
        
    def test_corner_cases(self):
        self.assertAlmostEqual(perimeter(0.5, 0.5), 2)
        self.assertAlmostEqual(perimeter(1.5, 2.5), 8)
        
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            perimeter("10", 5)
        with self.assertRaises(TypeError):
            perimeter(10, "5")
        with self.assertRaises(TypeError):
            perimeter("10", "5")
        with self.assertRaises(ValueError):
            perimeter(-10, 5)
        with self.assertRaises(ValueError):
            perimeter(10, -5)
        with self.assertRaises(ValueError):
            perimeter(-10, -5)
