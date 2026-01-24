import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(remove_empty([]), [])

    def test_single_empty_tuple(self):
        self.assertListEqual(remove_empty((None,)), [])

    def test_multiple_empty_tuples(self):
        self.assertListEqual(remove_empty(((), (), (None,), (), (1, None))), [(1,)])

    def test_single_empty_string_tuple(self):
        self.assertListEqual(remove_empty(('',)), [])

    def test_multiple_empty_string_tuples(self):
        self.assertListEqual(remove_empty(('', 'a', '', 'b', '', 'c')), ['a', 'b', 'c'])

    def test_mixed_empty_and_non_empty_tuples(self):
        self.assertListEqual(remove_empty(('', 'a', None, 'b', 1, ())), ['a', 'b', 1])

    def test_single_non_empty_tuple(self):
        self.assertListEqual(remove_empty(('a', 'b')), ['a', 'b'])

    def test_multiple_non_empty_tuples(self):
        self.assertListEqual(remove_empty((('a', 'b'), ('c', 'd'), ('e', 'f'))), [('a', 'b'), ('c', 'd'), ('e', 'f')])
