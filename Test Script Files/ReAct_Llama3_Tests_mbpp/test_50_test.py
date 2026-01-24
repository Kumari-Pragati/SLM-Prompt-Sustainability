import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(min_length_list([]), (0, []))

    def test_single_element_list(self):
        self.assertEqual(min_length_list([1]), (1, [1]))

    def test_multiple_element_list(self):
        self.assertEqual(min_length_list([1, 2, 3]), (1, [1]))

    def test_list_with_duplicates(self):
        self.assertEqual(min_length_list([1, 1, 2, 2, 3]), (1, [1]))

    def test_list_with_empty_strings(self):
        self.assertEqual(min_length_list(["", "a", "b"]), (0, [""]))

    def test_list_with_mixed_types(self):
        self.assertEqual(min_length_list([1, "a", 2, "b"]), (1, [1]))

    def test_list_with_negative_numbers(self):
        self.assertEqual(min_length_list([-1, -2, -3]), (3, [-3]))

    def test_list_with_zero_length_strings(self):
        self.assertEqual(min_length_list(["", "a", "b", "c"]), (0, [""]))

    def test_list_with_mixed_types_and_empty_strings(self):
        self.assertEqual(min_length_list(["", "a", 1, "b", 2]), (1, [1]))
