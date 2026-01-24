import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_nested(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_empty_tuple(self):
        self.assertEqual(remove_nested(()), ())

    def test_nested_tuple(self):
        self.assertEqual(remove_nested(('a', ('b', 'c'), 'd')), ('a', 'd'))

    def test_nested_tuple_with_empty_tuple(self):
        self.assertEqual(remove_nested(('a', (), 'b')), ('a', 'b'))

    def test_nested_tuple_with_single_element(self):
        self.assertEqual(remove_nested(('a', ('b',), 'c')), ('a', 'c'))

    def test_nested_tuple_with_single_element_at_nested_level(self):
        self.assertEqual(remove_nested(('a', ('b'), 'c')), ('a', 'c'))

    def test_nested_tuple_with_single_element_at_top_level(self):
        self.assertEqual(remove_nested(('a',), 'b'))

    def test_nested_tuple_with_single_element_at_bottom_level(self):
        self.assertEqual(remove_nested(('a', 'b'), 'c'))

    def test_nested_tuple_with_single_element_at_middle_level(self):
        self.assertEqual(remove_nested(('a', 'b', 'c'), 'd'))
