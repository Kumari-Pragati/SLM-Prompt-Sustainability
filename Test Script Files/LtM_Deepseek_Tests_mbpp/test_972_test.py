import unittest
from mbpp_972_code import concatenate_nested

class TestConcatenateNested(unittest.TestCase):

    def test_simple_concatenation(self):
        self.assertEqual(concatenate_nested((1, 2, 3), (4, 5, 6)), (1, 2, 3, 4, 5, 6))

    def test_empty_tuples(self):
        self.assertEqual(concatenate_nested((), ()), ())

    def test_one_empty_tuple(self):
        self.assertEqual(concatenate_nested((1, 2, 3), ()), (1, 2, 3))
        self.assertEqual(concatenate_nested((), (4, 5, 6)), (4, 5, 6))

    def test_large_tuples(self):
        large_tuple = tuple(range(1, 1001))
        self.assertEqual(concatenate_nested(large_tuple, large_tuple), large_tuple + large_tuple)

    def test_mixed_types(self):
        self.assertEqual(concatenate_nested((1, 'a', [1, 2, 3]), (4, 'b', [4, 5, 6])), 
                         (1, 'a', [1, 2, 3], 4, 'b', [4, 5, 6]))
