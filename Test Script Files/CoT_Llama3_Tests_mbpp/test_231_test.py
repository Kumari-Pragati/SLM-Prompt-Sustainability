import unittest
from mbpp_231_code import max_sum

class TestMaxSum(unittest.TestCase):
    def test_max_sum(self):
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(max_sum(tri, 3), 9)
        
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        self.assertEqual(max_sum(tri, 4), 12)
        
        tri = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
        self.assertEqual(max_sum(tri, 5), 15)
        
        tri = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(max_sum(tri, 2), 6)
        
        tri = [[1, 2, 3]]
        self.assertEqual(max_sum(tri, 1), 1)
        
        tri = [[1]]
        self.assertEqual(max_sum(tri, 1), 1)
        
        tri = []
        with self.assertRaises(IndexError):
            max_sum(tri, 1)
