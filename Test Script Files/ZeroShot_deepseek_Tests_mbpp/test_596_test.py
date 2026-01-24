import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 48)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), 56)

    def test_multiple_element_tuple(self):
        self.assertEqual(tuple_size((1, 2, 3, 4, 5)), 72)

    def test_large_tuple(self):
        self.assertGreater(tuple_size(tuple(range(10000))), 480000)
