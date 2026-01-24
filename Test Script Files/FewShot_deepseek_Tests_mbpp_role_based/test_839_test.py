import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(sort_tuple(((2, 'b'), (1, 'a'))), ((1, 'a'), (2, 'b')))

    def test_edge_condition(self):
        self.assertEqual(sort_tuple(((1, 'a'))), ((1, 'a')))

    def test_boundary_condition(self):
        self.assertEqual(sort_tuple(()), ())

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_tuple(123)

        with self.assertRaises(TypeError):
            sort_tuple('abc')

        with self.assertRaises(TypeError):
            sort_tuple([1, 2, 3])

        with self.assertRaises(TypeError):
            sort_tuple({'a': 1, 'b': 2})
