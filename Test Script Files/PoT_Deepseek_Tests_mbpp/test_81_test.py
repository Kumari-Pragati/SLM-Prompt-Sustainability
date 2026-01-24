import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(zip_tuples((1, 2, 3), ('a', 'b', 'c')), [(1, 'a'), (2, 'b'), (3, 'c')])

    def test_empty_tuples(self):
        self.assertEqual(zip_tuples((), ()), [])

    def test_different_lengths(self):
        self.assertEqual(zip_tuples((1, 2, 3), ('a', 'b')), [(1, 'a'), (2, 'b')])

    def test_single_element_tuples(self):
        self.assertEqual(zip_tuples((1,), ('a',)), [(1, 'a')])

    def test_large_tuples(self):
        self.assertEqual(zip_tuples(tuple(range(1000)), tuple('abc' * 334)), [(i, chr(j)) for i, j in enumerate(range(1000))])

    def test_negative_values(self):
        self.assertEqual(zip_tuples((-1, 0, 1), ('a', 'b', 'c')), [(-1, 'a'), (0, 'b'), (1, 'c')])
