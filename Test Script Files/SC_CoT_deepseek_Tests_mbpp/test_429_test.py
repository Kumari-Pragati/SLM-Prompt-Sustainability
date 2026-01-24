import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(and_tuples((1, 2, 3), (4, 5, 6)), ((1 & 4), (2 & 5), (3 & 6)))

    def test_empty_tuples(self):
        self.assertEqual(and_tuples((), ()), ())

    def test_single_element_tuples(self):
        self.assertEqual(and_tuples((1), (4)), (1 & 4,))

    def test_large_tuples(self):
        large_tuple = tuple(range(1, 10001))
        self.assertEqual(and_tuples(large_tuple, large_tuple), tuple(i & i for i in large_tuple))

    def test_mixed_types(self):
        with self.assertRaises(TypeError):
            and_tuples((1, 2, 3), ('4', '5', '6'))

    def test_unequal_length_tuples(self):
        with self.assertRaises(ValueError):
            and_tuples((1, 2, 3), (4, 5))
