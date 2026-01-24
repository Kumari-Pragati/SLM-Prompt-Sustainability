import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 48)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), 64)

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_size((1, 2, 3)), 80)

    def test_tuple_with_mixed_types(self):
        self.assertEqual(tuple_size((1, 'a', 3.14)), 96)

    def test_tuple_with_large_elements(self):
        large_elements = [i for i in range(1000)]
        self.assertEqual(tuple_size(tuple(large_elements)), 128)

    def test_non_tuple_input(self):
        with self.assertRaises(TypeError):
            tuple_size("not a tuple")

    def test_none_input(self):
        with self.assertRaises(TypeError):
            tuple_size(None)
