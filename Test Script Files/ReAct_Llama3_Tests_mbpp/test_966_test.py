import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(remove_empty(()), [])

    def test_single_element_tuple(self):
        self.assertEqual(remove_empty(('',)), ['',])

    def test_multiple_elements_tuple(self):
        self.assertEqual(remove_empty(('a', 'b', 'c')), ['a', 'b', 'c'])

    def test_empty_and_non_empty_elements_tuple(self):
        self.assertEqual(remove_empty(('', 'a', 'b')), ['', 'a', 'b'])

    def test_empty_tuple_with_duplicates(self):
        self.assertEqual(remove_empty(('', '',)), ['', ])

    def test_non_empty_tuple_with_duplicates(self):
        self.assertEqual(remove_empty(('a', 'a', 'b')), ['a', 'a', 'b'])

    def test_empty_tuple_with_empty_string(self):
        self.assertEqual(remove_empty(('', 'a', '')), ['', 'a', ''])

    def test_non_empty_tuple_with_empty_string(self):
        self.assertEqual(remove_empty(('a', 'b', '')), ['a', 'b', ''])
