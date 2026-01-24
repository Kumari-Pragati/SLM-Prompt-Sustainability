import unittest
from mbpp_272_code import rear_extract

class TestRearExtract(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(rear_extract([]), [])

    def test_single_element_list(self):
        self.assertListEqual(rear_extract([1]), [1])

    def test_multi_element_list(self):
        self.assertListEqual(rear_extract([1, 2, 3]), [3])

    def test_list_with_duplicates(self):
        self.assertListEqual(rear_extract([1, 2, 3, 2, 1]), [3, 2])

    def test_list_with_mixed_types(self):
        self.assertListEqual(rear_extract([1, 'a', 2, 'b']), [2, 'b'])
