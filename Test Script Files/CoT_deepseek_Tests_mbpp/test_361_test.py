import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_empty([1, '', 2, '', 3]), [1, 2, 3])

    def test_with_empty_strings(self):
        self.assertEqual(remove_empty(['', '', '']), [])

    def test_with_mixed_types(self):
        self.assertEqual(remove_empty([1, '', 'two', None, [], False]), [1, 'two', []])

    def test_with_none_elements(self):
        self.assertEqual(remove_empty([None, None, None]), [])

    def test_with_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_with_single_element(self):
        self.assertEqual(remove_empty([1]), [1])

    def test_with_empty_string_in_list(self):
        self.assertEqual(remove_empty(['']), [''])

    def test_with_boolean_values(self):
        self.assertEqual(remove_empty([True, False]), [True, False])

    def test_with_integer_values(self):
        self.assertEqual(remove_empty([1, 2, 3]), [1, 2, 3])

    def test_with_float_values(self):
        self.assertEqual(remove_empty([1.0, 2.0, 3.0]), [1.0, 2.0, 3.0])

    def test_with_mixed_numeric_types(self):
        self.assertEqual(remove_empty([1, 2.0, '3']), [1, 2.0, '3'])

    def test_with_nested_lists(self):
        self.assertEqual(remove_empty([[], [1, 2, 3], []]), [[1, 2, 3]])

    def test_with_list_of_lists(self):
        self.assertEqual(remove_empty([[1], [2], [3]]), [[1], [2], [3]])

    def test_with_empty_nested_lists(self):
        self.assertEqual(remove_empty([[], [], []]), [])

    def test_with_nested_empty_and_non_empty_lists(self):
        self.assertEqual(remove_empty([[], [1, 2, 3], []]), [[1, 2, 3]])

    def test_with_mixed_types_in_nested_lists(self):
        self.assertEqual(remove_empty([[1, ''], [2, ''], [3, '']]), [[1, ''], [2, ''], [3, '']])

    def test_with_empty_list_as_element(self):
        self.assertEqual(remove_empty([[], [], []]), [])

    def test_with_list_with_empty_list_as_element(self):
        self.assertEqual(remove_empty([[[]], [[]], [[]]]), [[]])

    def test_with_list_with_nested_empty_and_non_empty_lists(self):
        self.assertEqual(remove_empty([[[1, 2], []], [[3, 4], []], [[5, 6], []]]), [[[1, 2], []], [[3, 4], []], [[5, 6], []]])

    def test_with_list_with_mixed_types_in_nested_lists(self):
        self.assertEqual(remove_empty([[[1, ''], [2, '']], [[3, ''], [4, '']], [[5, ''], [6, '']]]), [[[1, ''], [2, '']], [[3, ''], [4, '']], [[5, ''], [6, '']]])
