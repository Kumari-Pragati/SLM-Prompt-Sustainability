import unittest
from mbpp_162_code import sum_series

class TestSumSeries(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(sum_series(5), 14)
        
    def test_edge_case(self):
        self.assertEqual(sum_series(1), 1)
        
    def test_boundary_case(self):
        self.assertEqual(sum_series(0), 0)
        self.assertEqual(sum_series(-1), 0)
        
    def test_special_case(self):
        self.assertEqual(sum_series(2), 3)
        
    def test_invalid_input(self):
        with self.assertRaises(RecursionError):
            sum_series(10000)
