import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_remove_empty_list(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_remove_empty_list_with_empty(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5, '']), [1, 2, 3, 4, 5])

    def test_remove_empty_list_with_empty_and_non_empty(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5, '', 6]), [1, 2, 3, 4, 5, 6])

    def test_remove_empty_list_with_empty_and_non_empty_and_empty(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5, '', 6, '']), [1, 2, 3, 4, 5, 6])

    def test_remove_empty_list_with_empty_and_non_empty_and_empty_and_non_empty(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5, '', 6, '', 7]), [1, 2, 3, 4, 5, 6, 7])

    def test_remove_empty_list_with_empty_and_non_empty_and_empty_and_non_empty_and_empty(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5, '', 6, '', 7, '']), [1, 2, 3, 4, 5, 6, 7])

    def test_remove_empty_list_with_empty_and_non_empty_and_empty_and_non_empty_and_empty_and_non_empty(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5, '', 6, '', 7, '', 8]), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_remove_empty_list_with_empty_and_non_empty_and_empty_and_non_empty_and_empty_and_non_empty_and_empty(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5, '', 6, '', 7, '', 8, '']), [1, 2, 3, 4, 5, 6, 7, 8])

    def test_remove_empty_list_with_empty_and_non_empty_and_empty_and_non_empty_and_empty_and_non_empty_and_empty_and_non_empty(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5, '', 6, '', 7, '', 8, '', 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
