import unittest
from903_code import count_Unset_Bits

class TestCountUnsetBits(unittest.TestCase):

    def test_zero(self):
        """Test for zero input"""
        self.assertEqual(count_Unset_Bits(0), 0)

    def test_one(self):
        """Test for single bit set input"""
        self.assertEqual(count_Unset_Bits(1), 1)

    def test_powers_of_two(self):
        """Test for powers of 2"""
        for i in range(1, 11):
            self.assertEqual(count_Unset_Bits(2**i), i - 1)

    def test_negative_number(self):
        """Test for negative number"""
        with self.assertRaises(ValueError):
            count_Unset_Bits(-1)

    def test_large_number(self):
        """Test for large number"""
        self.assertEqual(count_Unset_Bits(2**31 - 1), 31)
