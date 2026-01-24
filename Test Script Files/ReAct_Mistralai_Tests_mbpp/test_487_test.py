import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):

    def test_sort_ascending(self):
        self.assertEqual(sort_tuple((1, 'a')), ((1, 'a'),))
        self.assertEqual(sort_tuple((3, 'z'), (2, 'y'), (1, 'x')), ((1, 'x'), (2, 'y'), (3, 'z')))

    def test_sort_descending(self):
        self.assertEqual(sort_tuple((3, 'z'), reverse=True), ((3, 'z'),))
        self.assertEqual(sort_tuple((3, 'z'), (2, 'y'), (1, 'x'), reverse=True), ((1, 'x'), (2, 'y'), (3, 'z')))

    def test_empty_tuple(self):
        self.assertEqual(sort_tuple(()), ())

    def test_single_element_tuple(self):
        self.assertEqual(sort_tuple((1, 'a')), ((1, 'a'),))

    def test_mixed_type_tuple(self):
        self.assertRaises(TypeError, sort_tuple, (1, 'a', 2))

    def test_duplicate_tuples(self):
        self.assertEqual(sort_tuple(((1, 'a'), (1, 'b')), reverse=True), (((1, 'b'),), (1, 'a')))
