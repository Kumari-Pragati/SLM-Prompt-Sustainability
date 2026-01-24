import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_simple_list(self):
        self.assertListEqual(remove_empty([1, 2, 3, '', 4, None]), [1, 2, 3, 4])

    def test_empty_list(self):
        self.assertListEqual(remove_empty([]), [])

    def test_list_with_empty_string(self):
        self.assertListEqual(remove_empty(['a', '', 'b']), ['a', 'b'])

    def test_list_with_none(self):
        self.assertListEqual(remove_empty([1, None, 3]), [1, 3])

    def test_list_with_all_empty(self):
        self.assertListEqual(remove_empty([None, '', [], 0]), [])

    def test_list_with_all_non_empty(self):
        self.assertListEqual(remove_empty([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
