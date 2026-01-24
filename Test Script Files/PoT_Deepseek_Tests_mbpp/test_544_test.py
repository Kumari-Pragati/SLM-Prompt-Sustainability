import unittest
from mbpp_544_code import flatten_tuple

class TestFlattenTuple(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(flatten_tuple([(1, 2), (3, 4)]), '1 2 3 4')

    def test_empty_list(self):
        self.assertEqual(flatten_tuple([]), '')

    def test_single_tuple(self):
        self.assertEqual(flatten_tuple([(1, 2, 3)]), '1 2 3')

    def test_single_element_tuples(self):
        self.assertEqual(flatten_tuple([(1,), (2,), (3,)]), '1 2 3')

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            flatten_tuple([(1, 'a'), (2, 3)])
