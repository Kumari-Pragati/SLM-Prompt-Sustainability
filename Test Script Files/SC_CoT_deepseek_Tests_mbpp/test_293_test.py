import unittest
from mbpp_293_code import otherside_rightangle

class TestOthersideRightangle(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertAlmostEqual(otherside_rightangle(3,4), 5.0)
        
    def test_typical_case_2(self):
        self.assertAlmostEqual(otherside_rightangle(5,12), 13.0)
        
    def test_boundary_case(self):
        self.assertAlmostEqual(otherside_rightangle(0,0), 0.0)
        
    def test_edge_case(self):
        self.assertAlmostEqual(otherside_rightangle(1,math.sqrt(2)), math.sqrt(2))
        
    def test_negative_input(self):
        with self.assertRaises(ValueError):
            otherside_rightangle(-1,4)
            
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            otherside_rightangle('a', 4)
