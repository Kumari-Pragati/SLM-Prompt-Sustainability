import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 16)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), 24)

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_size((1, 2, 3, 4, 5)), 48)

    def test_large_tuple(self):
        large_tuple = tuple(range(1000))
        self.assertGreater(tuple_size(large_tuple), 48)

    def test_empty_list_as_input(self):
        self.assertRaises(TypeError, tuple_size, [])

    def test_string_as_input(self):
        self.assertRaises(TypeError, tuple_size, "abc")

    def test_set_as_input(self):
        self.assertRaises(TypeError, tuple_size, {1, 2, 3})
