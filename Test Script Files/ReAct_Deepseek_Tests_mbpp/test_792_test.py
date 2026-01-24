import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([1]), 1)

    def test_large_list(self):
        self.assertEqual(count_list(list(range(1, 1001))), 1000)

    def test_list_with_duplicates(self):
        self.assertEqual(count_list([1, 2, 2, 3, 4, 4, 5]), 7)

    def test_list_with_none_elements(self):
        self.assertEqual(count_list([None, 1, 2, 3, None]), 5)

    def test_list_with_mixed_types(self):
        self.assertEqual(count_list([1, 'two', 3.0, None, False]), 5)
