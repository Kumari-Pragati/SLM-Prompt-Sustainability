import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_empty([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_single_element_list(self):
        self.assertEqual(remove_empty([0]), [0])

    def test_multiple_empty_elements(self):
        self.assertEqual(remove_empty([0, '', None, [], {}]), [0])

    def test_non_empty_list(self):
        self.assertEqual(remove_empty(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_list_with_mixed_elements(self):
        self.assertEqual(remove_empty([1, 'a', 0, None, []]), [1, 'a', 0])

    def test_list_with_empty_string(self):
        self.assertEqual(remove_empty(['a', '', 'b']), ['a', 'b'])

    def test_list_with_empty_list(self):
        self.assertEqual(remove_empty([1, [], 2, 'a']), [1, 2, 'a'])

    def test_list_with_empty_dict(self):
        self.assertEqual(remove_empty([1, {}, 2, 'a']), [1, 2, 'a'])

    def test_list_with_empty_tuple(self):
        self.assertEqual(remove_empty([1, (), 2, 'a']), [1, 2, 'a'])

    def test_list_with_empty_set(self):
        self.assertEqual(remove_empty([1, set(), 2, 'a']), [1, 2, 'a'])
