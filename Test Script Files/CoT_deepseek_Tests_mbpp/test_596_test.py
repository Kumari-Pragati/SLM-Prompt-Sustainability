import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_typical_case(self):
        self.assertGreater(tuple_size((1, 2, 3)), 0)

    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 0)

    def test_large_tuple(self):
        large_tuple = tuple(range(10000))
        self.assertGreater(tuple_size(large_tuple), 0)

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tuple_size([])

    def test_nested_tuple(self):
        nested_tuple = ((1, 2), (3, 4))
        self.assertGreater(tuple_size(nested_tuple), 0)
