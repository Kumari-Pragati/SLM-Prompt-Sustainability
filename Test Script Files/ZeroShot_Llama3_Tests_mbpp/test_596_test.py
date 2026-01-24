import unittest
from mbpp_596_code import tuple_size

class TestTupleSize(unittest.TestCase):

    def test_tuple_size(self):
        # Test with empty tuple
        self.assertEqual(tuple_size(()), sys.getsizeof(()))

        # Test with single element tuple
        self.assertEqual(tuple_size((1,)), sys.getsizeof((1,)))

        # Test with multiple element tuple
        self.assertEqual(tuple_size((1, 2, 3)), sys.getsizeof((1, 2, 3)))

        # Test with mixed data type tuple
        self.assertEqual(tuple_size((1, 'a', 3.0)), sys.getsizeof((1, 'a', 3.0)))

        # Test with large tuple
        large_tuple = tuple(range(1000))
        self.assertEqual(tuple_size(large_tuple), sys.getsizeof(large_tuple))

    def test_tuple_size_with_non_tuple(self):
        # Test with non-tuple input
        with self.assertRaises(TypeError):
            tuple_size("")
