import unittest
from mbpp_27_code import remove

class TestRemove(unittest.TestCase):
    def test_remove_numbers(self):
        self.assertEqual(remove(['a1b2c3', 'd4e5f6']), ['ab', 'de'])

    def test_empty_list(self):
        self.assertEqual(remove([]), [])

    def test_single_item_list(self):
        self.assertEqual(remove(['a']), [''])

    def test_list_with_only_numbers(self):
        self.assertEqual(remove([1, 2, 3]), [])

    def test_list_with_only_strings(self):
        self.assertEqual(remove(['a', 'b', 'c']), ['', '', ''])
