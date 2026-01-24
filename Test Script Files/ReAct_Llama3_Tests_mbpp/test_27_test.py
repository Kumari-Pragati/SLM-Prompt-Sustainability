import unittest
from mbpp_27_code import remove

class TestRemoveFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(remove([]), [])

    def test_list_with_numbers(self):
        self.assertEqual(remove([1, 2, 3, 4, 5]), ['', '', '', '', ''])

    def test_list_with_letters(self):
        self.assertEqual(remove(['a', 'b', 'c', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])

    def test_list_with_mixed(self):
        self.assertEqual(remove(['a', 1, 'b', 2, 'c', 3, 'd', 4, 'e', 5]), ['', '', '', '', ''])

    def test_list_with_empty_strings(self):
        self.assertEqual(remove(['', 'b', '', 'd', 'e']), ['', 'b', '', 'd', 'e'])

    def test_list_with_single_element(self):
        self.assertEqual(remove(['hello']), ['hello'])

    def test_list_with_single_element_number(self):
        self.assertEqual(remove([123]), [''])

    def test_list_with_single_element_empty_string(self):
        self.assertEqual(remove(['']), [''])
