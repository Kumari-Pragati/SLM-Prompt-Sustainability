import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(remove_empty(()), [])

    def test_single_element(self):
        self.assertEqual(remove_empty(('',)), [''])

    def test_multiple_elements(self):
        self.assertEqual(remove_empty(('a', 'b', 'c')), ['a', 'b', 'c'])

    def test_empty_string(self):
        self.assertEqual(remove_empty(('', 'a', 'b')), ['', 'a', 'b'])

    def test_empty_string_and_empty_tuple(self):
        self.assertEqual(remove_empty(('', (), 'a', 'b')), ['', 'a', 'b'])

    def test_empty_string_and_empty_tuple_and_empty_string(self):
        self.assertEqual(remove_empty(('', (), '', 'a', 'b')), ['', 'a', 'b'])

    def test_empty_string_and_empty_tuple_and_empty_string_and_empty_tuple(self):
        self.assertEqual(remove_empty(('', (), '', '', 'a', 'b')), ['', 'a', 'b'])
