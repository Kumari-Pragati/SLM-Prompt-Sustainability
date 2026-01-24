import unittest
from mbpp_919_code import multiply_list

class TestMultiplyList(unittest.TestCase):

    def test_empty_list(self):
        """Test multiply_list with an empty list"""
        self.assertEqual(multiply_list([]), 1)

    def test_single_item(self):
        """Test multiply_list with a single item"""
        self.assertEqual(multiply_list([1]), 1)

    def test_positive_numbers(self):
        """Test multiply_list with multiple positive numbers"""
        self.assertEqual(multiply_list([1, 2, 3, 4]), 24)

    def test_negative_numbers(self):
        """Test multiply_list with multiple negative numbers"""
        self.assertEqual(multiply_list([-1, -2, -3, -4]), 24)

    def test_mixed_numbers(self):
        """Test multiply_list with a mix of positive and negative numbers"""
        self.assertEqual(multiply_list([1, -2, 3, -4]), -24)

    def test_zero(self):
        """Test multiply_list with zero"""
        self.assertEqual(multiply_list([0]), 0)
        self.assertEqual(multiply_list([0, 1, 2, 3]), 0)

    def test_floats(self):
        """Test multiply_list with floats"""
        self.assertAlmostEqual(multiply_list([1.1, 2.2, 3.3]), 7.056)

    def test_strings(self):
        """Test multiply_list with strings"""
        with self.assertRaises(TypeError):
            multiply_list(["a", "b", "c"])
