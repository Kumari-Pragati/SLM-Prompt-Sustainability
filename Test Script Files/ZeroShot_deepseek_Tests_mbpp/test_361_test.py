import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_remove_empty_with_non_empty_list(self):
        self.assertEqual(remove_empty([1, 2, 3]), [1, 2, 3])

    def test_remove_empty_with_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_remove_empty_with_mixed_list(self):
        self.assertEqual(remove_empty([1, '', 3]), [1, 3])

    def test_remove_empty_with_list_with_none(self):
        self.assertEqual(remove_empty([1, None, 3]), [1, None, 3])

    def test_remove_empty_with_list_with_false(self):
        self.assertEqual(remove_empty([1, False, 3]), [1, False, 3])
