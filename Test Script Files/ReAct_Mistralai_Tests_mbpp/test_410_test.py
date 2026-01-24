import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):

    def test_empty_list(self):
        """Test min_val with an empty list"""
        with self.assertRaises(TypeError):
            min_val([])

    def test_all_non_ints(self):
        """Test min_val with a list of non-ints"""
        self.assertIsNone(min_val(['a', 'b', 3]))

    def test_all_floats(self):
        """Test min_val with a list of floats"""
        self.assertAlmostEqual(min_val([3.14, 2.71, 1.61]), 1.61)

    def test_mixed_types(self):
        """Test min_val with a mixed list of ints and non-ints"""
        self.assertEqual(min_val([1, 'a', 2, 'b', 3]), 1)

    def test_min_int(self):
        """Test min_val with a list containing the minimum int value"""
        self.assertEqual(min_val([-9223372036854775808, -1, 0, 1]), -9223372036854775808)

    def test_min_float(self):
        """Test min_val with a list containing the minimum float value"""
        self.assertAlmostEqual(min_val([-float('inf'), -3.14, -1.0, 0.0, 1.0]), -float('inf'))
