import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_typical_case(self):
        self.assertLessEqual(tuple_size(()), 50)

    def test_large_tuple(self):
        large_tuple = tuple(range(1000))
        self.assertLessEqual(tuple_size(large_tuple), 9000)

    def test_empty_tuple(self):
        self.assertLessEqual(tuple_size(()), 50)

    def test_single_element_tuple(self):
        self.assertLessEqual(tuple_size((1,)), 50)

    def test_large_element_tuple(self):
        large_tuple = (1000000,)
        self.assertLessEqual(tuple_size(large_tuple), 8000)

    def test_nested_tuple(self):
        nested_tuple = ((), (1, 2, 3), (4, 5, 6))
        self.assertLessEqual(tuple_size(nested_tuple), 200)

    def test_string_tuple(self):
        string_tuple = ('a', 'b', 'c')
        self.assertLessEqual(tuple_size(string_tuple), 50)

    def test_tuple_with_none(self):
        tuple_with_none = (None,)
        self.assertLessEqual(tuple_size(tuple_with_none), 50)

    def test_tuple_with_float(self):
        tuple_with_float = (1.0,)
        self.assertLessEqual(tuple_size(tuple_with_float), 50)

    def test_tuple_with_boolean(self):
        tuple_with_boolean = (True,)
        self.assertLessEqual(tuple_size(tuple_with_boolean), 50)

    def test_tuple_with_complex(self):
        tuple_with_complex = (1+2j,)
        self.assertLessEqual(tuple_size(tuple_with_complex), 50)
