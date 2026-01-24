import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_tuple(('a', 'b', 'c')), ('a', 'b', 'c'))

    def test_duplicate_removal(self):
        self.assertEqual(remove_tuple(('a', 'b', 'a')), ('a', 'b'))

    def test_empty_input(self):
        self.assertEqual(remove_tuple(()), ())

    def test_single_element(self):
        self.assertEqual(remove_tuple(('a',)), ('a',))

    def test_large_input(self):
        self.assertEqual(remove_tuple(('a', 'b', 'c', 'a', 'b', 'c')), ('a', 'b', 'c'))

    def test_numeric_input(self):
        self.assertEqual(remove_tuple((1, 2, 3, 1)), (1, 2, 3))

    def test_mixed_input(self):
        self.assertEqual(remove_tuple(('a', 1, 'b', 1)), ('a', 1, 'b'))
