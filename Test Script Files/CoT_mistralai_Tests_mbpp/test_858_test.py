import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count_list([1, 2, 3]), 9)

    def test_list_with_duplicates(self):
        self.assertEqual(count_list([1, 1, 2, 2, 3]), 18)

    def test_list_with_negative_numbers(self):
        self.assertEqual(count_list([1, -2, 3]), 9)

    def test_list_with_floats(self):
        self.assertEqual(count_list([1.1, 2.2, 3.3]), 9)

    def test_list_with_strings(self):
        self.assertEqual(count_list(["a", "b", "c"]), 9)

    def test_list_with_mixed_types(self):
        self.assertEqual(count_list([1, "a", 2.0, True]), 9)

    def test_list_with_empty_elements(self):
        self.assertEqual(count_list([1, None, 2]), 9)

    def test_list_with_large_numbers(self):
        self.assertEqual(count_list([1000000001, 1000000002, 1000000003]), 10000000000)
