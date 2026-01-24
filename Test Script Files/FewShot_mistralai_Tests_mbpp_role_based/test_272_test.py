import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(rear_extract([]), [])

    def test_single_element_list(self):
        self.assertListEqual(rear_extract([1]), [1])

    def test_multiple_element_lists(self):
        self.assertListEqual(rear_extract([1, 2, 3]), [3, 2, 1])

    def test_list_with_duplicates(self):
        self.assertListEqual(rear_extract([1, 2, 1, 3]), [3, 1])

    def test_list_with_non_list_elements(self):
        self.assertRaises(TypeError, rear_extract, [1, 2, 'a'])
