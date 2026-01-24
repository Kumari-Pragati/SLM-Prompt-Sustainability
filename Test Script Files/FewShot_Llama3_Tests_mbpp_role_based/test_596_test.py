import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):
    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), sys.getsizeof(()))

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), sys.getsizeof((1,)))

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_size((1, 2, 3)), sys.getsizeof((1, 2, 3)))

    def test_tuple_with_mixed_types(self):
        self.assertEqual(tuple_size((1, "hello", 3.14)), sys.getsizeof((1, "hello", 3.14)))

    def test_tuple_with_large_elements(self):
        large_elements = [i for i in range(1000)]
        self.assertEqual(tuple_size(tuple(large_elements)), sys.getsizeof(tuple(large_elements)))

    def test_tuple_with_nested_tuples(self):
        nested_tuple = ((1, 2), (3, 4))
        self.assertEqual(tuple_size(nested_tuple), sys.getsizeof(nested_tuple))
