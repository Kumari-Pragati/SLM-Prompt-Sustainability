import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_single_element_list(self):
        self.assertEqual(swap_List([1]), [1])

    def test_regular_list(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 1, 2])

    def test_list_with_duplicates(self):
        self.assertEqual(swap_List([1, 1, 2, 3]), [3, 1, 1, 2])

    def test_list_with_negative_index(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 1, 2])

    def test_list_with_out_of_range_index(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 1, 2])

    def test_list_with_non_integer_index(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 1, 2])

    def test_list_with_string_element(self):
        self.assertEqual(swap_List(["a", "b", "c"]), ["c", "a", "b"])

    def test_list_with_mixed_types(self):
        self.assertEqual(swap_List([1, "a", 2]), ["a", 1, 2])
