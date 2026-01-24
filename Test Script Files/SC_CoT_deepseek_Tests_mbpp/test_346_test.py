import unittest
from mbpp_346_code import zigzag

class TestZigzag(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(zigzag(3, 2), 3)
        
    def test_boundary_case(self):
        self.assertEqual(zigzag(0, 0), 1)
        self.assertEqual(zigzag(5, 0), 0)
        self.assertEqual(zigzag(0, 5), 0)
        
    def test_edge_case(self):
        self.assertEqual(zigzag(1, 1), 1)
        self.assertEqual(zigzag(2, 1), 1)
        self.assertEqual(zigzag(2, 2), 1)
        
    def test_special_case(self):
        self.assertEqual(zigzag(4, 2), 4)
        self.assertEqual(zigzag(3, 1), 3)
        
    def test_invalid_input(self):
        with self.assertRaises(Exception):
            zigzag(-1, 2)
        with self.assertRaises(Exception):
            zigzag(1, -2)
        with self.assertRaises(Exception):
            zigzag(-1, -2)
