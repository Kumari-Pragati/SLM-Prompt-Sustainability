import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_empty([1, 2, 3, None, '', 'a', 0]), [1, 2, 3, 'a'])

    def test_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_single_empty_element(self):
        self.assertEqual(remove_empty(['', 1, 2, 3]), [1, 2, 3])

    def test_list_of_empty_strings(self):
        self.assertEqual(remove_empty(['', '', '']), [])

    def test_list_of_none(self):
        self.assertEqual(remove_empty([None, None, None]), [])

    def test_list_of_numbers(self):
        self.assertEqual(remove_empty([1, 2, 3, 0, None]), [1, 2, 3, 0])
