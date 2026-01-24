import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(remove_nested(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_empty_input(self):
        self.assertEqual(remove_nested(()), ())

    def test_nested_input(self):
        self.assertEqual(remove_nested(('a', ('b', 'c'), 'd')), ('a', 'd'))

    def test_nested_mixed_input(self):
        self.assertEqual(remove_nested(('a', 1, ('b', 'c'), 2)), ('a', 1, 'b', 2))

    def test_nested_deep_input(self):
        self.assertEqual(remove_nested(('a', ('b', ('c', 'd')), 'e')), ('a', 'e'))
