import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_simple_tuple(self):
        self.assertEqual(tuple_size((1, 2, 3)), 48)

    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 48)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), 48)

    def test_large_tuple(self):
        self.assertEqual(tuple_size((1,) * 1000), 48000)

    def test_tuple_with_complex_objects(self):
        self.assertEqual(tuple_size(([1, 2, 3], (1, 2, 3), {1, 2, 3}, "abc", None)), 104)
