import unittest
from mbpp_791_code import remove_nested

class TestRemoveNested(unittest.TestCase):

    def test_remove_nested(self):
        self.assertEqual(remove_nested(('a', 'b', 'c')), ('a', 'b', 'c'))
        self.assertEqual(remove_nested(('a', ('b', 'c'), 'd')), ('a', 'd'))
        self.assertEqual(remove_nested(('a', ('b', ('c', 'd')), 'e')), ('a', 'e'))
        self.assertEqual(remove_nested(('a', 'b', ('c', 'd'), 'e')), ('a', 'b', 'e'))
        self.assertEqual(remove_nested(('a', ('b', ('c', 'd'), 'e'), 'f')), ('a', 'f'))
        self.assertEqual(remove_nested(('a', 'b', 'c', ('d', 'e'), 'f')), ('a', 'b', 'c', 'f'))
