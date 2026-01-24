import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(remove_empty([]), [])

    def test_single_empty_element(self):
        self.assertListEqual(remove_empty([None, 1, '', 3]), [1, 3])

    def test_multiple_empty_elements(self):
        self.assertListEqual(remove_empty([None, '', 0, 'a', None, 'b', 1, None]), ['a', 'b', 1])

    def test_all_empty_elements(self):
        self.assertListEqual(remove_empty([None, '', 0]), [])

    def test_list_with_only_empty_elements(self):
        self.assertListEqual(remove_empty([None, '', 0]), [])
