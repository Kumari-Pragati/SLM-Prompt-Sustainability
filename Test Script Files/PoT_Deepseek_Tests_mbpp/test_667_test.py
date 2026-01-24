import unittest
from mbpp_667_code import Check_Vow

class TestCheckVow(unittest.TestCase):
    
    def test_typical_cases(self):
        self.assertEqual(Check_Vow("hello", "aeiou"), 2)
        self.assertEqual(Check_Vow("AEIOU", "aeiou"), 5)
        self.assertEqual(Check_Vow("AEIOUaeiou", "AEIOUaeiou"), 10)
        
    def test_edge_cases(self):
        self.assertEqual(Check_Vow("", "aeiou"), 0)
        self.assertEqual(Check_Vow("bcdfghjklmnpqrstvwxyz", "aeiou"), 0)
        
    def test_boundary_cases(self):
        self.assertEqual(Check_Vow("AEIOU", "aeiouAEIOU"), 10)
        self.assertEqual(Check_Vow("AEIOUaeiou", ""), 0)
        
    def test_corner_cases(self):
        self.assertEqual(Check_Vow("AEIOUaeiou", "AEIOUaeiou"), 10)
        self.assertEqual(Check_Vow("AEIOUaeiou", "AEIOUaeiouAEIOU"), 15)
        self.assertEqual(Check_Vow("AEIOUaeiou", "bcdfghjklmnpqrstvwxyz"), 0)
