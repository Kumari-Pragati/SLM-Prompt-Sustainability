import unittest
from mbpp_487_code import sort_tuple

class TestSortTuple(unittest.TestCase):
    def test_sort_ascending(self):
        self.assertEqual(sort_tuple((1, 'a')), ((1, 'a'),))
        self.assertEqual(sort_tuple((3, 'b'), (2, 'a')), ((2, 'a'), (3, 'b')))

    def test_sort_descending(self):
        self.assertEqual(sort_tuple((3, 'b'), (2, 'a'), reverse=True), ((3, 'b'), (2, 'a')))

    def test_empty_list(self):
        self.assertEqual(sort_tuple([]), [])

    def test_single_element(self):
        self.assertEqual(sort_tuple((1, 'a')), ((1, 'a'),))

    def test_mixed_types(self):
        self.assertEqual(sort_tuple((1, 'a'), (2, 'b'), (3, 4)), ((1, 'a'), (2, 'b'), (3, 4)))

    def test_duplicates(self):
        self.assertEqual(sort_tuple((1, 'a'), (1, 'b')), ((1, 'a'), (1, 'b')))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sort_tuple(1)
