import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], rear_extract([]))

    def test_single_element_list(self):
        self.assertListEqual([42], rear_extract([42]))

    def test_multiple_element_lists(self):
        self.assertListEqual([3, 2], rear_extract([[1, 2, 3], [4, 5, 3, 2]]))

    def test_list_with_only_one_list(self):
        self.assertListEqual([42], rear_extract([[42]]))

    def test_list_with_empty_lists(self):
        self.assertListEqual([], rear_extract([[], [42], [1, 2, 3]]))

    def test_list_with_non_list_elements(self):
        with self.assertRaises(TypeError):
            rear_extract([42, "test", 3.14])

    def test_list_with_negative_index(self):
        with self.assertRaises(IndexError):
            rear_extract([[42], [-1]])
