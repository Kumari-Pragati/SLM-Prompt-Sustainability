import unittest
from mbpp_203_code import hamming_Distance

class TestHammingDistance(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(hamming_Distance(1, 4), 2)
        
    def test_same_number(self):
        self.assertEqual(hamming_Distance(5, 5), 0)
        
    def test_edge_case_zero(self):
        self.assertEqual(hamming_Distance(0, 0), 0)
        
    def test_boundary_case_max_int(self):
        self.assertEqual(hamming_Distance(2147483647, 2147483647), 0)
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            hamming_Distance("1", 4)
        with self.assertRaises(TypeError):
            hamming_Distance(1, "4")
        with self.assertRaises(TypeError):
            hamming_Distance("1", "4")
