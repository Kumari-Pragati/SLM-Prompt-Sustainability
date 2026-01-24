import unittest
from mbpp_549_code import odd_Num_Sum

class TestOddNumSum(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(odd_Num_Sum(5), 110400)
        
    def test_boundary_case(self):
        self.assertEqual(odd_Num_Sum(1), 1)
        
    def test_edge_case(self):
        self.assertEqual(odd_Num_Sum(0), 0)
        self.assertEqual(odd_Num_Sum(-1), 0)
        
    def test_special_case(self):
        self.assertEqual(odd_Num_Sum(10), 167961600)
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            odd_Num_Sum('a')
        with self.assertRaises(TypeError):
            odd_Num_Sum(None)
        with self.assertRaises(TypeError):
            odd_Num_Sum([])
