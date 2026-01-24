import unittest
from mbpp_612_code import merge

class TestMergeFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(merge([[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])

    def test_empty_list(self):
        self.assertEqual(merge([]), [])

    def test_single_list(self):
        self.assertEqual(merge([[1, 2, 3]]), [[1], [2], [3]])

    def test_different_length_lists(self):
        self.assertEqual(merge([[1, 2], [3]]), [[1, 3], [2]])

    def test_empty_sublists(self):
        self.assertEqual(merge([[], []]), [[]])

    def test_single_element_sublists(self):
        self.assertEqual(merge([[1], [2]]), [[1], [2]])

    def test_large_input(self):
        large_input = [[i for i in range(10)] for _ in range(10)]
        expected_output = [[i for i in range(10)] for _ in range(10)]
        self.assertEqual(merge(large_input), expected_output)
