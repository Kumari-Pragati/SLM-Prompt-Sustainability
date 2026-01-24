import unittest
from mbpp_240_code import replace_list

class TestReplaceList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(replace_list([1, 2, 3], [4, 5]), [1, 2, 4, 5])

    def test_empty_list1(self):
        self.assertEqual(replace_list([], [4, 5]), [4, 5])

    def test_empty_list2(self):
        self.assertEqual(replace_list([1, 2, 3], []), [1, 2, 3])

    def test_single_element_list2(self):
        self.assertEqual(replace_list([1, 2, 3], [4]), [1, 2, 4])

    def test_large_list2(self):
        self.assertEqual(replace_list([1, 2, 3], [4, 5, 6, 7]), [1, 2, 4, 5, 6, 7])

    def test_negative_numbers(self):
        self.assertEqual(replace_list([1, 2, 3], [-1, -2, -3]), [1, 2, -1, -2, -3])
