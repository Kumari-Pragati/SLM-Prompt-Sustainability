import unittest
from mbpp_558_code import digit_distance_nums

class TestDigitDistanceNums(unittest.TestCase):
    
    def test_typical_case(self):
        self.assertEqual(digit_distance_nums(123, 456), 5)
        
    def test_same_number(self):
        self.assertEqual(digit_distance_nums(123, 123), 0)
        
    def test_negative_numbers(self):
        self.assertEqual(digit_distance_nums(-123, 456), 10)
        
    def test_large_numbers(self):
        self.assertEqual(digit_distance_nums(123456789, 987654321), 24)
        
    def test_zero(self):
        self.assertEqual(digit_distance_nums(0, 123), 3)
        
    def test_equal_digits(self):
        self.assertEqual(digit_distance_nums(111, 111), 0)
        
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            digit_distance_nums("123", 456)
