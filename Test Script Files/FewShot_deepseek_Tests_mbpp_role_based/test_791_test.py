import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_nested(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_typical_use_case_with_nested_tuples(self):
        self.assertEqual(remove_nested(('a', ('b', 'c'), 'd')), ('a', 'd'))

    def test_empty_tuple(self):
        self.assertEqual(remove_nested(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(remove_nested(('a',)), ('a',))

    def test_tuple_with_nested_tuple_at_end(self):
        self.assertEqual(remove_nested(('a', 'b', ('c',))), ('a', 'b'))

    def test_tuple_with_nested_tuple_at_start(self):
        self.assertEqual(remove_nested((('a',), 'b', 'c')), ('b', 'c'))

    def test_tuple_with_only_nested_tuples(self):
        self.assertEqual(remove_nested((('a', 'b'), ('c', 'd'))), ())
