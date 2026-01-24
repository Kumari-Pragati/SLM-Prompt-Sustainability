import unittest
from mbpp_193_code import remove_tuple

class TestRemoveTuple(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_tuple(('a', 'b', 'c')), (('a', 'b', 'c'),))

    def test_edge_condition(self):
        self.assertEqual(remove_tuple(()), ((),))

    def test_boundary_condition(self):
        self.assertEqual(remove_tuple(('a',)), (('a',),))

    def test_duplicate_elements(self):
        self.assertEqual(remove_tuple(('a', 'a', 'b')), (('a', 'b'),))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_tuple(123)
