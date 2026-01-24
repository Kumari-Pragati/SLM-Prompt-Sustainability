import unittest
from mbpp_612_code import merge

class TestMerge(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(merge([[1, 2], [3, 4], [5, 6]]), [[1, 3, 5], [2, 4, 6]])

    def test_empty_list(self):
        self.assertEqual(merge([]), [])

    def test_single_list(self):
        self.assertEqual(merge([[1, 2, 3]]), [[1], [2], [3]])

    def test_different_length_lists(self):
        self.assertEqual(merge([[1, 2], [3]]), [[1, 3], [2]])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            merge(123)
        with self.assertRaises(TypeError):
            merge('123')
        with self.assertRaises(TypeError):
            merge([1, 2, 3, 'a'])
