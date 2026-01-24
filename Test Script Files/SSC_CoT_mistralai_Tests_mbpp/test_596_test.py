import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(tuple_size((1, 2, 3)), 48)

    def test_empty_input(self):
        self.assertEqual(tuple_size(()), 48)

    def test_single_input(self):
        self.assertEqual(tuple_size((42,)), 40)

    def test_large_input(self):
        large_tuple = tuple(range(10000))
        self.assertGreater(tuple_size(large_tuple), 48)

    def test_mixed_types(self):
        self.assertRaises(TypeError, tuple_size, (1, 2, 3.0, "str"))

    def test_list_input(self):
        self.assertRaises(TypeError, tuple_size, [1, 2, 3])
