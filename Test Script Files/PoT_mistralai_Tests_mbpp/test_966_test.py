import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertListEqual(remove_empty(()), [])

    def test_single_empty_tuple(self):
        self.assertListEqual(remove_empty(()), [])

    def test_single_empty_string(self):
        self.assertListEqual(remove_empty(('',)), [])

    def test_single_non_empty_string(self):
        self.assertListEqual(remove_empty(('a',)), ['a'])

    def test_multiple_non_empty_elements(self):
        self.assertListEqual(remove_empty(('a', 'b', 'c')), ['a', 'b', 'c'])

    def test_single_empty_list(self):
        self.assertListEqual(remove_empty([None]], [])

    def test_single_non_empty_list(self):
        self.assertListEqual(remove_empty([1]), [1])

    def test_single_empty_dict(self):
        self.assertListEqual(remove_empty({}), [])

    def test_single_non_empty_dict(self):
        self.assertListEqual(remove_empty({'key': 'value'}), [{'key': 'value'}])
