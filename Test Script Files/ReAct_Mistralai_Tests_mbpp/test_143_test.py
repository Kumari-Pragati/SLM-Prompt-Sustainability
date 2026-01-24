import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):

    def test_empty_list(self):
        """Tests if an empty list is correctly identified as a list"""
        self.assertEqual(find_lists([]), 1)

    def test_single_element_list(self):
        """Tests if a list with a single element is correctly identified as a list"""
        self.assertEqual(find_lists([1]), 1)

    def test_multiple_elements_list(self):
        """Tests if a list with multiple elements is correctly identified as a list"""
        self.assertEqual(find_lists([1, 2, 3]), 1)

    def test_list_with_duplicates(self):
        """Tests if a list with duplicates is correctly identified as a list"""
        self.assertEqual(find_lists([1, 1, 2, 3]), 1)

    def test_list_with_complex_elements(self):
        """Tests if a list with complex elements (e.g., lists, tuples, dictionaries) is correctly identified as a list"""
        self.assertEqual(find_lists([1, [2, 3], (4, 5), {"a": 1}]), 1)

    def test_string_input(self):
        """Tests if a string input is correctly identified as non-list"""
        self.assertEqual(find_lists("Hello"), len("Hello"))

    def test_integer_input(self):
        """Tests if an integer input is correctly identified as non-list"""
        self.assertEqual(find_lists(42), len(str(42)))

    def test_float_input(self):
        """Tests if a float input is correctly identified as non-list"""
        self.assertEqual(find_lists(3.14), len(str(3.14)))

    def test_tuple_input(self):
        """Tests if a tuple input is correctly identified as non-list"""
        self.assertEqual(find_lists((1, 2, 3)), len((1, 2, 3)))

    def test_dict_input(self):
        """Tests if a dictionary input is correctly identified as non-list"""
        self.assertEqual(find_lists({"a": 1, "b": 2}), len({"a": 1, "b": 2}))
