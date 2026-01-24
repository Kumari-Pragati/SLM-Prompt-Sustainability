import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(tuple_size(()), 56)
        self.assertEqual(tuple_size((1, 2, 3)), 56 + 3 * 24)
        self.assertEqual(tuple_size(('a', 'b', 'c')), 56 + 3 * 24)

    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 56)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), 56 + 24)

    def test_large_tuple(self):
        large_tuple = tuple(range(1000))
        self.assertGreater(tuple_size(large_tuple), 56 + 1000 * 24)

    def test_nested_tuple(self):
        self.assertEqual(tuple_size((('a', 'b'), ('c', 'd'))), 56 + 2 * (24 + 2 * 24))

    def test_tuple_with_subtuples(self):
        self.assertEqual(tuple_size(((1, 2), (3, 4))), 56 + 2 * (24 + 2 * 24))
