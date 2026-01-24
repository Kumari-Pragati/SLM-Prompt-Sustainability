import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_remove_empty(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_empty([1, 2, '', 4, 5]), [1, 2, 4, 5])
        self.assertEqual(remove_empty([1, 2, 3, 4, '', 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_empty(['', '', '', '', '']), [])
        self.assertEqual(remove_empty([1, 2, 3, 4, 5, '']), [1, 2, 3, 4, 5])
        self.assertEqual(remove_empty([1, 2, '', 4, '', 5]), [1, 2, 4, 5])

    def test_remove_empty_with_non_string_elements(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_empty([1, 2, 3, 4, 5.5]), [1, 2, 3, 4, 5.5])
        self.assertEqual(remove_empty([1, 2, 3, 4, 5, 6.7]), [1, 2, 3, 4, 5, 6.7])
