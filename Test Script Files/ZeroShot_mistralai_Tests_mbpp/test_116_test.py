import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_int([]), 0)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_to_int([1]), 1)
        self.assertEqual(tuple_to_int([-1]), -1)

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_to_int([1, 2, 3]), 123)
        self.assertEqual(tuple_to_int([-1, -2, -3]), -123)
        self.assertEqual(tuple_to_int([0, 0, 0]), 0)

    def test_large_numbers(self):
        self.assertEqual(tuple_to_int([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]), 9876543210)
        self.assertEqual(tuple_to_int([-9, -8, -7, -6, -5, -4, -3, -2, -1, -0]), -9876543210)
