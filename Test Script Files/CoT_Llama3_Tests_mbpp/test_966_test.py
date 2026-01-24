import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(remove_empty(()), [])

    def test_single_empty_element(self):
        self.assertEqual(remove_empty(('',)), [''])

    def test_multiple_empty_elements(self):
        self.assertEqual(remove_empty(('', '',)), [])

    def test_non_empty_elements(self):
        self.assertEqual(remove_empty(('a', 'b', 'c')), ['a', 'b', 'c'])

    def test_mixed_elements(self):
        self.assertEqual(remove_empty(('', 'a', 'b', 'c')), ['a', 'b', 'c'])

    def test_empty_list(self):
        self.assertEqual(remove_empty([]), [])

    def test_empty_list_with_non_empty_elements(self):
        self.assertEqual(remove_empty([('',), ('a',), ('b',)]), ['a', 'b'])
