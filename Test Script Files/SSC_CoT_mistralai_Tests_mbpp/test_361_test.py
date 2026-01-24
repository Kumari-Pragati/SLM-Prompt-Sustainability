import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(remove_empty([1, 2, 3, '', 4, None, 'abc']), [1, 2, 3, 4, 'abc'])

    def test_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_all_empty_strings(self):
        self.assertEqual(remove_empty(['', ' ', '\t', '\n', '\r']), [])

    def test_all_none(self):
        self.assertEqual(remove_empty([None, None, None]), [])

    def test_all_falsy(self):
        self.assertEqual(remove_empty([False, 0, '', None, [], (), {}]), [])

    def test_single_empty_string(self):
        self.assertEqual(remove_empty(['abc', '', 'def']), ['abc', 'def'])

    def test_single_empty_list(self):
        self.assertEqual(remove_empty([[], 'abc']), ['abc'])
