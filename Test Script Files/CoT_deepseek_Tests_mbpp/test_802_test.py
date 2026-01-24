import unittest
from mbpp_802_code import count_Rotation

class TestCountRotation(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(count_Rotation([15, 18, 2, 3, 6, 12], 6), 2)
        
    def test_single_element(self):
        self.assertEqual(count_Rotation([1], 1), 0)
        
    def test_already_sorted(self):
        self.assertEqual(count_Rotation([1, 2, 3, 4, 5], 5), 0)
        
    def test_empty_array(self):
        self.assertEqual(count_Rotation([], 0), 0)
        
    def test_large_array(self):
        self.assertEqual(count_Rotation([5, 6, 7, 1, 2, 3, 4], 7), 3)
        
    def test_negative_numbers(self):
        self.assertEqual(count_Rotation([-15, -10, -5, 0, 5, 10], 6), 4)
        
    def test_duplicate_elements(self):
        self.assertEqual(count_Rotation([1, 1, 2, 2, 1, 1], 6), 2)
        
    def test_rotated_array(self):
        self.assertEqual(count_Rotation([3, 4, 5, 1, 2], 5), 3)
