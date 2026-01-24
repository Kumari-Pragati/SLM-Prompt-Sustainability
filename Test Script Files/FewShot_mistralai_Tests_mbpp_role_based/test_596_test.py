import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 0)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), 24)

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_size((1, 2, 3, 4, 5)), 48)

    def test_large_tuple(self):
        large_tuple = tuple(range(10000))
        self.assertGreater(tuple_size(large_tuple), 100000)
