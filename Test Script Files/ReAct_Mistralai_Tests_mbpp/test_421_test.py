import unittest
from mbpp_421_code import concatenate_tuple

class TestConcatenateTuple(unittest.TestCase):

    def test_empty_tuple(self):
        """Test concatenating an empty tuple"""
        result = concatenate_tuple(())
        self.assertEqual(result, "")

    def test_single_element_tuple(self):
        """Test concatenating a single-element tuple"""
        result = concatenate_tuple((1))
        self.assertEqual(result, "1")

    def test_multiple_elements_tuple(self):
        """Test concatenating a multi-element tuple"""
        result = concatenate_tuple((1, 2, 3))
        self.assertEqual(result, "1-2-3")

    def test_negative_integer_tuple(self):
        """Test concatenating a tuple with negative integers"""
        result = concatenate_tuple((-1, -2, -3))
        self.assertEqual(result, "-1-2-3")

    def test_mixed_types_tuple(self):
        """Test concatenating a tuple with mixed types"""
        with self.assertRaises(TypeError):
            concatenate_tuple(("a", 1, None))

    def test_delimiter_change(self):
        """Test changing the delimiter"""
        result = concatenate_tuple((1, 2, 3), delim=".")
        self.assertEqual(result, "1.2.3")
