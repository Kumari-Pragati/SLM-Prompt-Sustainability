import unittest
from mbpp_890_code import find_Extra

class TestFindExtra(unittest.TestCase):
    def test_find_extra_with_same_elements(self):
        self.assertEqual(find_Extra([1, 2, 3, 4], [1, 2, 3, 4], 4), 4)

    def test_find_extra_with_different_elements(self):
        self.assertEqual(find_Extra([1, 2, 3, 4], [1, 2, 5, 4], 4), 2)

    def test_find_extra_with_empty_arrays(self):
        self.assertEqual(find_Extra([], [], 0), 0)

    def test_find_extra_with_one_element_arrays(self):
        self.assertEqual(find_Extra([1], [1], 1), 0)
        self.assertEqual(find_Extra([1], [2], 1), 0)

    def test_find_extra_with_negative_index(self):
        with self.assertRaises(IndexError):
            find_Extra([1, 2, 3], [1, 2, 3], -1)
