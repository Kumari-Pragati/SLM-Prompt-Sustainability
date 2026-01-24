import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(zip_tuples((1, 2, 3), ('a', 'b', 'c')), [(1, 'a'), (2, 'b'), (3, 'c')])

    def test_empty_tuples(self):
        self.assertEqual(zip_tuples((), ()), [])

    def test_different_length_tuples(self):
        self.assertEqual(zip_tuples((1, 2, 3), ('a', 'b')), [(1, 'a'), (2, 'b')])

    def test_long_tuple2(self):
        self.assertEqual(zip_tuples((1, 2, 3), ('a', 'b', 'c', 'd', 'e')), [(1, 'a'), (2, 'b'), (3, 'c')])

    def test_single_element_tuples(self):
        self.assertEqual(zip_tuples((1,), ('a',)), [(1, 'a')])

    def test_negative_values(self):
        self.assertEqual(zip_tuples((-1, 2, 3), ('a', 'b', 'c')), [(-1, 'a'), (2, 'b'), (3, 'c')])

    def test_zero_values(self):
        self.assertEqual(zip_tuples((0, 2, 3), ('a', 'b', 'c')), [(0, 'a'), (2, 'b'), (3, 'c')])

    def test_large_numbers(self):
        self.assertEqual(zip_tuples((1000, 2000, 3000), ('a', 'b', 'c')), [(1000, 'a'), (2000, 'b'), (3000, 'c')])

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            zip_tuples([1, 2, 3], ('a', 'b', 'c'))
