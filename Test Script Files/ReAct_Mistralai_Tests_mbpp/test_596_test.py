import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_empty_tuple(self):
        """Test empty tuple"""
        self.assertEqual(tuple_size(()), 0)

    def test_single_element_tuple(self):
        """Test single element tuple"""
        self.assertEqual(tuple_size((1,)), 24)

    def test_multiple_elements_tuple(self):
        """Test multiple elements tuple"""
        self.assertEqual(tuple_size((1, 2, 3, 4, 5)), 48)

    def test_large_tuple(self):
        """Test large tuple"""
        large_tuple = tuple(range(10000))
        self.assertGreater(tuple_size(large_tuple), 48000)

    def test_tuple_with_none(self):
        """Test tuple with None"""
        self.assertEqual(tuple_size((None, 1, 2)), 32)

    def test_tuple_with_string(self):
        """Test tuple with string"""
        self.assertEqual(tuple_size(('Hello', 1, 2)), 48)

    def test_tuple_with_list(self):
        """Test tuple with list"""
        self.assertEqual(tuple_size(((1, 2, 3), 4, 5)), 48)

    def test_tuple_with_dict(self):
        """Test tuple with dictionary"""
        self.assertEqual(tuple_size(((dict(a=1, b=2)), 3, 4)), 48)

    def test_tuple_with_set(self):
        """Test tuple with set"""
        self.assertEqual(tuple_size(((set([1, 2, 3]), 4, 5)), 48)
