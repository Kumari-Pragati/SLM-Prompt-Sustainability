import unittest
from mbpp_735_code import toggle_middle_bits

class TestToggleMiddleBits(unittest.TestCase):

    def test_empty(self):
        """Test if function works correctly with zero"""
        self.assertEqual(toggle_middle_bits(0), 1)

    def test_powers_of_two(self):
        """Test if function works correctly with powers of 2"""
        for i in range(1, 32):
            self.assertEqual(toggle_middle_bits(1 << i), 1 << (i - 1))

    def test_negative_numbers(self):
        """Test if function works correctly with negative numbers"""
        self.assertEqual(toggle_middle_bits(-1), 0)
        self.assertEqual(toggle_middle_bits(-2), 1)

    def test_large_numbers(self):
        """Test if function works correctly with large numbers"""
        max_int = (1 << 31) - 1
        self.assertEqual(toggle_middle_bits(max_int), 0)

    def test_one(self):
        """Test if function returns 1 for input 1"""
        self.assertEqual(toggle_middle_bits(1), 1)
