import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):

    def test_empty_list(self):
        """Test sum_elements with an empty list"""
        self.assertEqual(sum_elements([]), 0)

    def test_single_element(self):
        """Test sum_elements with a single element"""
        self.assertEqual(sum_elements((1,)), 1)

    def test_multiple_elements(self):
        """Test sum_elements with multiple elements"""
        self.assertEqual(sum_elements((1, 2, 3, 4, 5)), 15)

    def test_negative_numbers(self):
        """Test sum_elements with negative numbers"""
        self.assertEqual(sum_elements((-1, 0, 1)), 0)

    def test_large_numbers(self):
        """Test sum_elements with large numbers"""
        self.assertEqual(sum_elements((1000000, 2000000, 3000000)), 6000000)

    def test_float_numbers(self):
        """Test sum_elements with float numbers"""
        self.assertAlmostEqual(sum_elements((1.1, 2.2, 3.3)), 6.6)

    def test_mixed_types(self):
        """Test sum_elements with mixed types"""
        with self.assertRaises(TypeError):
            sum_elements((1, 'a', [2]))
