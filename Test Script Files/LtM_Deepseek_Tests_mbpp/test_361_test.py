import unittest
from mbpp_361_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(remove_empty([1, 2, 3]), [1, 2, 3])
        self.assertEqual(remove_empty(['a', 'b', 'c']), ['a', 'b', 'c'])

    def test_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_list_with_empty_elements(self):
        self.assertEqual(remove_empty([1, '', 3]), [1, 3])
        self.assertEqual(remove_empty(['a', '', 'c']), ['a', 'c'])

    def test_list_with_none_elements(self):
        self.assertEqual(remove_empty([1, None, 3]), [1, 3])
        self.assertEqual(remove_empty(['a', None, 'c']), ['a', 'c'])

    def test_list_with_mixed_elements(self):
        self.assertEqual(remove_empty([0, '', None, [], 'a', '']), [0, 'a'])
