import unittest
from mbpp_839_code import sort_tuple

class TestSortTuple(unittest.TestCase):
    def test_sort_ascending(self):
        self.assertEqual(sort_tuple((('a', 1), ('b', 2), ('c', 3))), (('a', 1), ('b', 2), ('c', 3)))
        self.assertEqual(sort_tuple((('z', 1), ('y', 2), ('x', 3))), (('x', 3), ('y', 2), ('z', 1)))

    def test_sort_descending(self):
        self.assertEqual(sort_tuple((('z', 1), ('y', 2), ('x', 3)), reverse=True), (('x', 3), ('y', 2), ('z', 1)))
        self.assertEqual(sort_tuple((('a', 1), ('b', 2), ('c', 3)), reverse=True), (('c', 3), ('b', 2), ('a', 1)))

    def test_empty_list(self):
        self.assertEqual(sort_tuple([]), [])

    def test_single_item(self):
        self.assertEqual(sort_tuple((('a', 1))), (('a', 1)))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            sort_tuple((('a', 1), 2))
        with self.assertRaises(TypeError):
            sort_tuple((2, ('a', 1)))

    def test_duplicate_tuples(self):
        self.assertEqual(sort_tuple((('a', 1), ('a', 2))), (('a', 1), ('a', 2)))
