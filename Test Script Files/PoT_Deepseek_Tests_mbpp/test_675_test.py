import unittest
from mbpp_675_code import sum_nums

class TestSumNums(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(sum_nums(5, 10, 15, 30), 15)
        
    def test_boundary_case(self):
        self.assertEqual(sum_nums(10, 10, 20, 30), 20)
        
    def test_edge_case(self):
        self.assertEqual(sum_nums(15, 15, 30, 45), 20)
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum_nums('a', 10, 20, 30)
            
    def test_negative_numbers(self):
        self.assertEqual(sum_nums(-5, -10, -15, -3), -15)
        
    def test_sum_equals_boundary(self):
        self.assertEqual(sum_nums(10, 10, 20, 30), 20)
        
    def test_sum_greater_than_boundary(self):
        self.assertEqual(sum_nums(15, 15, 30, 45), 20)
