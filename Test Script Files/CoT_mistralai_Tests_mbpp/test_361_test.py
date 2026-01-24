import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(remove_empty([]), [])

    def test_list_with_empty_elements(self):
        self.assertListEqual(remove_empty([1, None, 3, '', 5]), [1, 3, 5])

    def test_list_with_only_empty_elements(self):
        self.assertListEqual(remove_empty(['', ' ', '\t', '\n']), [])

    def test_list_with_single_empty_element(self):
        self.assertListEqual(remove_empty([1, '', 3]), [1, 3])

    def test_list_with_multiple_empty_elements(self):
        self.assertListEqual(remove_empty([1, '', 3, '', 5]), [1, 3, 5])

    def test_list_with_only_empty_strings(self):
        self.assertListEqual(remove_empty(['', 'a', 'b', '']), ['a', 'b'])

    def test_list_with_non_empty_strings(self):
        self.assertListEqual(remove_empty(['a', 'b', 'c', '', 'd']), ['a', 'b', 'c', 'd'])
