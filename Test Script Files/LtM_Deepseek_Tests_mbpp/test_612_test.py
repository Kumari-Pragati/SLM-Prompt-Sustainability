import unittest
from mbpp_612_code import merge

class TestMergeFunction(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(merge([[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])

    def test_empty_input(self):
        self.assertEqual(merge([]), [])

    def test_single_list_input(self):
        self.assertEqual(merge([[1, 2, 3]]), [[1], [2], [3]])

    def test_two_lists_of_different_lengths(self):
        self.assertEqual(merge([[1, 2], [3]]), [[1, 3], [2]])

    def test_input_with_empty_sublists(self):
        self.assertEqual(merge([[], []]), [[]])

    def test_input_with_single_element_sublists(self):
        self.assertEqual(merge([[1], [2], [3]]), [[1, 2, 3]])
