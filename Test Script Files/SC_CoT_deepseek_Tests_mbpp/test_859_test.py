import unittest
from mbpp_859_code import sub_lists

class TestSubLists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sub_lists([1, 2, 3]), [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])

    def test_empty_list(self):
        self.assertEqual(sub_lists([]), [[]])

    def test_single_element(self):
        self.assertEqual(sub_lists([1]), [[], [1]])

    def test_duplicate_elements(self):
        self.assertEqual(sub_lists([1, 2, 2]), [[], [1], [2], [2], [1, 2], [1, 2], [2, 2], [1, 2, 2]])

    def test_large_list(self):
        self.assertEqual(len(sub_lists(list(range(1, 10)))), 1024)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sub_lists(123)
