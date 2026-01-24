import unittest
from mbpp_80_code import tetrahedral_number

class TestTetrahedralNumber(unittest.TestCase):

    def test_positive_integer(self):
        """Test tetrahedral number for positive integers"""
        self.assertEqual(tetrahedral_number(1), 0)
        self.assertEqual(tetrahedral_number(2), 1)
        self.assertEqual(tetrahedral_number(3), 4)
        self.assertEqual(tetrahedral_number(10), 105)

    def test_zero(self):
        """Test tetrahedral number for zero"""
        self.assertEqual(tetrahedral_number(0), 0)

    def test_negative_integer(self):
        """Test tetrahedral number for negative integers"""
        self.assertEqual(tetrahedral_number(-1), 0)
        self.assertEqual(tetrahedral_number(-2), -1)
        self.assertEqual(tetrahedral_number(-3), -12)

    def test_large_integer(self):
        """Test tetrahedral number for large integers"""
        self.assertEqual(tetrahedral_number(1000), 5005000005)

    def test_non_integer(self):
        """Test tetrahedral number for non-integer inputs"""
        with self.assertRaises(TypeError):
            tetrahedral_number(3.14)
