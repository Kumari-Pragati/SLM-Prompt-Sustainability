import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_nested(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_nested_tuple(self):
        self.assertEqual(remove_nested(('a', ('b', 'c'), 'd')), ('a', 'd'))

    def test_empty_tuple(self):
        self.assertEqual(remove_nested(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(remove_nested(('a',)), ('a',))

    def test_nested_tuple_with_empty_tuple(self):
        self.assertEqual(remove_nested(('a', (), 'b')), ('a', 'b'))

    def test_nested_tuple_with_single_element_tuple(self):
        self.assertEqual(remove_nested(('a', ('b'), 'c')), ('a', 'c'))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_nested(123)
