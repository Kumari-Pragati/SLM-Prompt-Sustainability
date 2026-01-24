import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_length_list([1, 2, 3]), (1, [1]))

    def test_empty_list(self):
        self.assertEqual(max_length_list([]), (0, []))

    def test_single_element(self):
        self.assertEqual(max_length_list([1]), (1, [1]))

    def test_multiple_elements(self):
        self.assertEqual(max_length_list([1, 2, 3, 4, 5]), (5, [5]))

    def test_list_with_duplicates(self):
        self.assertEqual(max_length_list([1, 2, 2, 3, 4, 5]), (5, [5]))

    def test_list_with_empty_elements(self):
        self.assertEqual(max_length_list([1, 2, '', 4, 5]), (5, [5]))

    def test_list_with_mixed_types(self):
        self.assertEqual(max_length_list([1, 2, 'a', 4, 5]), (5, [5]))
