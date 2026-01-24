import unittest
from mbpp_739_code import find_Index

class TestFindIndex(unittest.TestCase):

    def test_find_index_positive(self):
        """Test find_Index with positive integer inputs"""
        self.assertAlmostEqual(find_Index(1), 1.0, delta=0.01)
        self.assertAlmostEqual(find_Index(2), 2.0, delta=0.01)
        self.assertAlmostEqual(find_Index(10), 5.0, delta=0.01)

    def test_find_index_zero(self):
        """Test find_Index with zero input"""
        self.assertEqual(find_Index(0), 0.0)

    def test_find_index_negative(self):
        """Test find_Index with negative integer inputs"""
        self.assertRaises(ValueError, find_Index, -1)

    def test_find_index_large_input(self):
        """Test find_Index with large integer inputs"""
        self.assertAlmostEqual(find_Index(1000), 500.0, delta=0.01)
        self.assertRaises(ValueError, find_Index, 1000000)
