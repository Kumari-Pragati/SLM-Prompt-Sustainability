import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(tuple_size(()), 0)

    def test_single_element_tuple(self):
        self.assertEqual(tuple_size((1,)), sys.getsizeof((1,)) + sys.getsizeof(tuple()))

    def test_multiple_elements_tuple(self):
        self.assertEqual(tuple_size((1, 2, 3)), sys.getsizeof((1, 2, 3)) + 3 * sys.getsizeof(tuple(1)) + sys.getsizeof(tuple()))

    def test_tuple_with_mixed_types(self):
        self.assertEqual(tuple_size(('a', 1, 3.14)), sys.getsizeof(('a', 1, 3.14)) + sys.getsizeof(tuple('a')) + sys.getsizeof(tuple((1,))) + sys.getsizeof(tuple((3.14,))) + sys.getsizeof(tuple()))

    def test_large_tuple(self):
        large_tuple = tuple(range(10000))
        self.assertGreater(tuple_size(large_tuple), 10000)
