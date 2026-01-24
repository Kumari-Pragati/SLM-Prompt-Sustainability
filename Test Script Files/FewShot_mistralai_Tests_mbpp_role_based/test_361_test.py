import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_list_with_empty_elements(self):
        self.assertEqual(remove_empty([1, None, 3, '', 5]), [1, 3, 5])

    def test_list_with_only_empty_elements(self):
        self.assertEqual(remove_empty([None, '', 0]), [])

    def test_list_with_mixed_empty_and_non_empty_elements(self):
        self.assertEqual(remove_empty([1, None, 3, '', 5, 'a']), [1, 3, 5, 'a'])
