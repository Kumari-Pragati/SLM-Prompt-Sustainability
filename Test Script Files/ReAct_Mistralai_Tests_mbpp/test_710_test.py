import unittest
from mbpp_710_code import front_and_rear

class TestFrontAndRear(unittest.TestCase):

    def test_empty_list(self):
        """Test front_and_rear with an empty list"""
        with self.assertRaises(IndexError):
            front_and_rear([])

    def test_single_element(self):
        """Test front_and_rear with a single element list"""
        result = front_and_rear([1])
        self.assertEqual(result, (1, 1))

    def test_multiple_elements(self):
        """Test front_and_rear with multiple elements list"""
        result = front_and_rear([1, 2, 3])
        self.assertEqual(result, (1, 3))

    def test_negative_numbers(self):
        """Test front_and_rear with negative numbers"""
        result = front_and_rear([-1, 0, 1])
        self.assertEqual(result, (-1, 1))

    def test_mixed_types(self):
        """Test front_and_rear with mixed types"""
        with self.assertRaises(TypeError):
            front_and_rear([1, "a", 3])
