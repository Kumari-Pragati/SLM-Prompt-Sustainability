import unittest
from mbpp_224_code import count_Set_Bits

class TestCountSetBits(unittest.TestCase):

    def test_zero(self):
        """Test for zero input"""
        self.assertEqual(count_Set_Bits(0), 0)

    def test_one(self):
        """Test for one input"""
        self.assertEqual(count_Set_Bits(1), 1)

    def test_powers_of_two(self):
        """Test for powers of two"""
        for i in range(1, 16):
            self.assertEqual(count_Set_Bits(2**i), i)

    def test_negative_numbers(self):
        """Test for negative numbers"""
        self.assertEqual(count_Set_Bits(-1), 1)
        self.assertEqual(count_Set_Bits(-3), 1)

    def test_large_positive_number(self):
        """Test for large positive number"""
        self.assertEqual(count_Set_Bits(2**31 - 1), 31)

    def test_large_negative_number(self):
        """Test for large negative number"""
        self.assertEqual(count_Set_Bits(-(2**31)), 31)

    def test_bitwise_combinations(self):
        """Test for bitwise combinations"""
        self.assertEqual(count_Set_Bits(3), 2)
        self.assertEqual(count_Set_Bits(5), 2)
        self.assertEqual(count_Set_Bits(7), 3)
        self.assertEqual(count_Set_Bits(9), 2)
        self.assertEqual(count_Set_Bits(11), 3)
        self.assertEqual(count_Set_Bits(13), 3)
        self.assertEqual(count_Set_Bits(15), 4)
