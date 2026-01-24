import unittest
from mbpp_143_code import find_lists

class TestFindLists(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(find_lists([]), 1)

    def test_single_element_list(self):
        self.assertEqual(find_lists([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(find_lists([1, 2, 3]), 3)

    def test_list_with_empty_list(self):
        self.assertEqual(find_lists([[], 1, 2]), 3)

    def test_list_with_tuple(self):
        self.assertEqual(find_lists([(1, 2), 3]), 2)

    def test_list_with_dictionary(self):
        self.assertEqual(find_lists([{'a': 1}, 3]), 2)

    def test_list_with_string(self):
        self.assertEqual(find_lists(['str', 3]), 2)

    def test_list_with_float(self):
        self.assertEqual(find_lists([3.14, 3]), 2)

    def test_list_with_set(self):
        self.assertEqual(find_lists([{1}, 3]), 2)

    def test_list_with_set_and_string(self):
        self.assertEqual(find_lists([{1}, 'str', 3]), 3)
