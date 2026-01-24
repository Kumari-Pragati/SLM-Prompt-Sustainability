import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_typical_case(self):
        self.assertLessEqual(tuple_size(()), 56)
        self.assertLessEqual(tuple_size((1,)), 64)
        self.assertLessEqual(tuple_size((1, 2, 3)), 72)

    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 56)

    def test_single_element_tuple(self):
        self.assertLessEqual(tuple_size((1,)), 64)

    def test_multiple_element_tuple(self):
        self.assertLessEqual(tuple_size((1, 2, 3)), 72)

    def test_large_tuple(self):
        large_tuple = tuple(range(1000))
        self.assertLessEqual(tuple_size(large_tuple), 8000)

    def test_large_tuple_with_large_elements(self):
        large_tuple = tuple(range(100000))
        self.assertLessEqual(tuple_size(large_tuple), 800000)

    def test_tuple_with_large_elements(self):
        large_tuple = tuple(range(10000))
        self.assertLessEqual(tuple_size(large_tuple), 80000)
