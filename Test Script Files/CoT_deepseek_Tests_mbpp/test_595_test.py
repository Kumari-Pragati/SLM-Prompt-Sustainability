import unittest
from mbpp_595_code import min_Swaps

class TestMinSwaps(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(min_Swaps('abc', 'bca'), 1)
        
    def test_edge_case(self):
        self.assertEqual(min_Swaps('abc', 'abc'), 0)
        
    def test_boundary_case(self):
        self.assertEqual(min_Swaps('a', 'a'), 0)
        self.assertEqual(min_Swaps('ab', 'ba'), 1)
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Swaps(123, 'abc')
        with self.assertRaises(TypeError):
            min_Swaps('abc', 123)
        with self.assertRaises(TypeError):
            min_Swaps(123, 456)
            
    def test_not_possible_case(self):
        self.assertEqual(min_Swaps('abc', 'def'), 'Not Possible')
