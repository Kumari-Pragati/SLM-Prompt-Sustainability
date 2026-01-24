import unittest
from mbpp_544_code import flatten_tuple

class TestFlattenTuple(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(flatten_tuple([(1, 2), (3, 4)]), '1 2 3 4')

    def test_empty_input(self):
        self.assertEqual(flatten_tuple([]), '')

    def test_single_tuple_input(self):
        self.assertEqual(flatten_tuple([(1, 2, 3)]), '1 2 3')

    def test_mixed_types_input(self):
        with self.assertRaises(TypeError):
            flatten_tuple([(1, '2', 3)])

    def test_nested_tuple_input(self):
        self.assertEqual(flatten_tuple([((1, 2), (3, 4))]), '1 2 3 4')

    def test_large_input(self):
        self.assertEqual(flatten_tuple([(i for i in range(1, 10001))]), ' '.join(map(str, range(1, 10001))))
