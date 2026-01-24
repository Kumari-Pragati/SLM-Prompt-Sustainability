import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(two_unique_nums([1, 2, 1, 3, 2, 5]), [3, 5])
        
    def test_empty_list(self):
        self.assertEqual(two_unique_nums([]), [])
        
    def test_single_element(self):
        self.assertEqual(two_unique_nums([1]), [1])
        
    def test_all_duplicates(self):
        self.assertEqual(two_unique_nums([1, 1, 1, 1]), [])
        
    def test_negative_numbers(self):
        self.assertEqual(two_unique_nums([-1, -2, -1, -3, -2, -5]), [-3, -5])
        
    def test_large_numbers(self):
        self.assertEqual(two_unique_nums([1000, 2000, 1000, 3000, 2000, 5000]), [3000, 5000])
        
    def test_mixed_numbers(self):
        self.assertEqual(two_unique_nums([-1, 2, -1, 3, 2, 5]), [3, 5])
