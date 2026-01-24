import unittest
from mbpp_612_code import merge

class TestMergeFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(merge([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [[1, 4, 7], [2, 5, 8], [3, 6, 9]])

    def test_empty_list(self):
        self.assertEqual(merge([]), [])

    def test_single_list(self):
        self.assertEqual(merge([[1, 2, 3]]), [[1], [2], [3]])

    def test_different_length_lists(self):
        self.assertEqual(merge([[1, 2], [3, 4, 5]]), [[1, 3], [2, 4], [5]])

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            merge(123)
        with self.assertRaises(TypeError):
            merge([1, 2, 3, 4])
        with self.assertRaises(TypeError):
            merge([[1, 2], 'a', [3, 4]])
