import unittest
from mbpp_885_code import is_Isomorphic

class TestIsIsomorphic(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertTrue(is_Isomorphic('egg', 'add'))
        
    def test_edge_case(self):
        self.assertTrue(is_Isomorphic('', ''))
        
    def test_special_case(self):
        self.assertFalse(is_Isomorphic('foo', 'bar'))
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_Isomorphic(123, 'add')
