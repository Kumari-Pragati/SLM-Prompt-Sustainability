import unittest
from mbpp_880_code import Check_Solution

class TestCheckSolution(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(Check_Solution(1, -3, 2), "2 solutions")
        
    def test_edge_case_positive_delta(self):
        self.assertEqual(Check_Solution(1, 2, 1), "1 solution")
        
    def test_edge_case_zero_delta(self):
        self.assertEqual(Check_Solution(1, 2, 1), "1 solution")
        
    def test_edge_case_negative_delta(self):
        self.assertEqual(Check_Solution(1, 2, 3), "No solutions")
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Check_Solution("a", "b", "c")
