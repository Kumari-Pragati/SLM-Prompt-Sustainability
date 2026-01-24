import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):

    def test_empty_list(self):
        """Tests that an empty list returns an empty tuple"""
        self.assertIsInstance(list_tuple([]), tuple)
        self.assertEqual(list_tuple([]), ())

    def test_single_element_list(self):
        """Tests that a list with one element returns a tuple with one element"""
        self.assertIsInstance(list_tuple([42]), tuple)
        self.assertEqual(list_tuple([42]), (42,))

    def test_multiple_elements_list(self):
        """Tests that a list with multiple elements returns a tuple with multiple elements"""
        self.assertIsInstance(list_tuple([1, 2, 3]), tuple)
        self.assertEqual(list_tuple([1, 2, 3]), (1, 2, 3))

    def test_list_with_duplicates(self):
        """Tests that a list with duplicates returns a tuple with duplicates"""
        self.assertIsInstance(list_tuple([1, 1, 2, 2, 3]), tuple)
        self.assertEqual(list_tuple([1, 1, 2, 2, 3]), (1, 1, 2, 2, 3))

    def test_list_with_non_numeric_element(self):
        """Tests that a list with non-numeric elements returns a tuple with non-numeric elements"""
        self.assertIsInstance(list_tuple(['a', 'b', 1]), tuple)
        self.assertEqual(list_tuple(['a', 'b', 1]), ('a', 'b', 1))

    def test_list_with_mixed_types(self):
        """Tests that a list with mixed types returns a tuple with mixed types"""
        self.assertIsInstance(list_tuple([1, 'a', 3.14]), tuple)
        self.assertEqual(list_tuple([1, 'a', 3.14]), (1, 'a', 3.14))

    def test_list_with_large_integer(self):
        """Tests that a list with a large integer returns a tuple with a large integer"""
        self.assertIsInstance(list_tuple([sys.maxsize + 1]), tuple)
        self.assertEqual(list_tuple([sys.maxsize + 1]), (sys.maxsize + 1,))

    def test_list_with_negative_integer(self):
        """Tests that a list with a negative integer returns a tuple with a negative integer"""
        self.assertIsInstance(list_tuple([-sys.maxsize - 1]), tuple)
        self.assertEqual(list_tuple([-sys.maxsize - 1]), (-sys.maxsize - 1,))
