import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_concatenate_simple_tuples(self):
        self.assertEqual(concatenate_nested((1, 2), (3, 4)), (1, 2, 3, 4))
        self.assertEqual(concatenate_nested(('a', 'b'), ('c', 'd')), ('a', 'b', 'c', 'd'))
        self.assertEqual(concatenate_nested((1.0, 2.0), (3.0, 4.0)), (1.0, 2.0, 3.0, 4.0))

    def test_concatenate_mixed_types(self):
        self.assertEqual(concatenate_nested((1, 2), ('a', 'b')), (1, 2, 'a', 'b'))
        self.assertEqual(concatenate_nested(('a', 'b'), (1, 2)), ('a', 'b', 1, 2))
        self.assertEqual(concatenate_nested((1, 2), (1.0, 2.0)), (1, 2, 1.0, 2.0))

    def test_concatenate_empty_tuples(self):
        self.assertEqual(concatenate_nested((), (1, 2)), (1, 2))
        self.assertEqual(concatenate_nested((1, 2),()), (1, 2))
        self.assertEqual(concatenate_nested((),()), ())

    def test_concatenate_single_input(self):
        self.assertEqual(concatenate_nested((1, 2)), (1, 2))
        self.assertEqual(concatenate_nested(('a', 'b')), ('a', 'b'))
        self.assertEqual(concatenate_nested((1.0, 2.0)), (1.0, 2.0))
