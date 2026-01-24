import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(zip_tuples((1, 2, 3), ('a', 'b', 'c')), [(1, 'a'), (2, 'b'), (3, 'c')])

    def test_empty_tuples(self):
        self.assertEqual(zip_tuples((), ()), [])

    def test_different_length_tuples(self):
        self.assertEqual(zip_tuples((1, 2, 3), ('a', 'b')), [(1, 'a'), (2, 'b')])

    def test_single_element_tuples(self):
        self.assertEqual(zip_tuples((1,), ('a',)), [(1, 'a')])

    def test_large_tuples(self):
        test_tup1 = tuple(range(1, 1001))
        test_tup2 = tuple('a' * 1000)
        self.assertEqual(zip_tuples(test_tup1, test_tup2)[:10], list(zip(test_tup1[:10], test_tup2[:10])))
