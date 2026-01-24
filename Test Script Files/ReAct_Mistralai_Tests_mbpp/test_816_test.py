import unittest
from mbpp_816_code import clear_tuple

class TestClearTuple(unittest.TestCase):

    def test_empty_tuple(self):
        """Test clearing an empty tuple"""
        result = clear_tuple(())
        self.assertIsInstance(result, tuple)
        self.assertListEqual(result, [])

    def test_single_element_tuple(self):
        """Test clearing a tuple with one element"""
        result = clear_tuple((1,))
        self.assertIsInstance(result, tuple)
        self.assertListEqual(result, [])

    def test_multiple_elements_tuple(self):
        """Test clearing a tuple with multiple elements"""
        result = clear_tuple((1, 2, 3))
        self.assertIsInstance(result, tuple)
        self.assertListEqual(result, [])

    def test_tuple_with_none(self):
        """Test clearing a tuple with None element"""
        result = clear_tuple((1, None, 3))
        self.assertIsInstance(result, tuple)
        self.assertListEqual(result, [None])

    def test_tuple_with_mixed_types(self):
        """Test clearing a tuple with mixed types"""
        result = clear_tuple((1, 'str', 3.0, None))
        self.assertIsInstance(result, tuple)
        self.assertListEqual(result, [1, 'str', 3.0])

    def test_tuple_with_list(self):
        """Test clearing a tuple containing a list"""
        result = clear_tuple(([1],))
        self.assertIsInstance(result, tuple)
        self.assertListEqual(result, [[]])
