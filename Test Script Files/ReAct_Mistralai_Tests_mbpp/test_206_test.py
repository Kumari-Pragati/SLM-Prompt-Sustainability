import unittest
from mbpp_206_code import concatenate_elements

class TestConcatenateElements(unittest.TestCase):

    def test_empty_tuple(self):
        """Test concatenate_elements on empty tuple"""
        with self.assertRaises(TypeError):
            concatenate_elements(())

    def test_single_element_tuple(self):
        """Test concatenate_elements on single element tuple"""
        result = concatenate_elements((1,))
        self.assertEqual(result, (1,))

    def test_normal_tuple(self):
        """Test concatenate_elements on normal tuple"""
        result = concatenate_elements((1, 2, 3, 4))
        self.assertEqual(result, (2, 3, 4))

    def test_tuple_with_single_element_at_end(self):
        """Test concatenate_elements on tuple with single element at end"""
        result = concatenate_elements((1, 2, 3, 4, 5))
        self.assertEqual(result, (2, 3, 4))

    def test_tuple_with_negative_numbers(self):
        """Test concatenate_elements on tuple with negative numbers"""
        result = concatenate_elements((-1, 0, 1, 2))
        self.assertEqual(result, (0, 1, 2))

    def test_tuple_with_mixed_types(self):
        """Test concatenate_elements on tuple with mixed types"""
        with self.assertRaises(TypeError):
            concatenate_elements((1, "2", 3))
