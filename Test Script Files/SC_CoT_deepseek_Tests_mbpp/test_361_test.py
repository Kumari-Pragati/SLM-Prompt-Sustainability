import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_empty([1, '', 2, '', 3]), [1, 2, 3])

    def test_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_list_with_only_empty_strings(self):
        self.assertEqual(remove_empty(['', '', '']), [])

    def test_list_with_mixed_types(self):
        self.assertEqual(remove_empty([0, '', None, [], {}]), [0, None, {}])

    def test_list_with_none_elements(self):
        self.assertEqual(remove_empty([None, None, None]), [])

    def test_list_with_single_empty_string(self):
        self.assertEqual(remove_empty(['']), [])

    def test_list_with_single_non_empty_string(self):
        self.assertEqual(remove_empty(['hello']), ['hello'])

    def test_list_with_single_zero(self):
        self.assertEqual(remove_empty([0]), [0])

    def test_list_with_single_none(self):
        self.assertEqual(remove_empty([None]), [])

    def test_list_with_single_empty_list(self):
        self.assertEqual(remove_empty([[]]), [[]])

    def test_list_with_single_empty_dict(self):
        self.assertEqual(remove_empty([{}]), [{}])
