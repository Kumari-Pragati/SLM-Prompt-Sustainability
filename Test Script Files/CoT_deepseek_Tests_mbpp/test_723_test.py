import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)
        
    def test_empty_lists(self):
        self.assertEqual(count_same_pair([], []), 0)
        
    def test_different_lengths(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2]), 2)
        
    def test_mixed_types(self):
        self.assertEqual(count_same_pair([1, '2', 3], [1, '2', 3]), 2)
        
    def test_same_elements(self):
        self.assertEqual(count_same_pair([1, 1, 1], [1, 1, 1]), 3)
        
    def test_different_elements(self):
        self.assertEqual(count_same_pair([1, 2, 3], [4, 5, 6]), 0)
        
    def test_negative_numbers(self):
        self.assertEqual(count_same_pair([-1, -2, -3], [-1, -2, -3]), 3)
        
    def test_zero(self):
        self.assertEqual(count_same_pair([0, 0, 0], [0, 0, 0]), 3)
        
    def test_large_numbers(self):
        self.assertEqual(count_same_pair([1000000, 2000000, 3000000], [1000000, 2000000, 3000000]), 3)
