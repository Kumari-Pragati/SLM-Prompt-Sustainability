import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_empty_tuple(self):
        """Test empty tuple"""
        with self.assertRaises(TypeError):
            multiply_elements(())

    def test_single_element_tuple(self):
        """Test single element tuple"""
        self.assertEqual(multiply_elements((1,)), (1,))

    def test_two_elements_tuple(self):
        """Test two elements tuple"""
        self.assertEqual(multiply_elements((1, 2)), (2, 2))

    def test_three_elements_tuple(self):
        """Test three elements tuple"""
        self.assertEqual(multiply_elements((1, 2, 3)), (2, 4, 3))

    def test_negative_numbers(self):
        """Test negative numbers"""
        self.assertEqual(multiply_elements((-1, 2)), (2, -4))

    def test_zero(self):
        """Test zero"""
        self.assertEqual(multiply_elements((0, 2)), (0, 0))

    def test_float_numbers(self):
        """Test float numbers"""
        self.assertAlmostEqual(multiply_elements((1.5, 2)), (3, 4))

    def test_mixed_types(self):
        """Test mixed types"""
        with self.assertRaises(TypeError):
            multiply_elements((1, "2"))
