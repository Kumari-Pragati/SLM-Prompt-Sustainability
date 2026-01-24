import unittest
from mbpp_589_code import perfect_squares

class TestPerfectSquares(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(perfect_squares(1, 10), [1, 4, 9])
        
    def test_single_square(self):
        self.assertEqual(perfect_squares(4, 4), [4])
        
    def test_no_squares(self):
        self.assertEqual(perfect_squares(10, 15), [])
        
    def test_negative_range(self):
        self.assertEqual(perfect_squares(-10, 10), [1, 4, 9])
        
    def test_zero_and_one(self):
        self.assertEqual(perfect_squares(0, 1), [0, 1])
        
    def test_large_range(self):
        self.assertEqual(perfect_squares(1000, 1100), [1024])
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            perfect_squares("1", 10)
