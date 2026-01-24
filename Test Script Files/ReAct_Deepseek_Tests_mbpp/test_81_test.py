import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):

    def test_typical_case(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = ('a', 'b', 'c')
        expected_output = [(1, 'a'), (2, 'b'), (3, 'c')]
        self.assertEqual(zip_tuples(test_tup1, test_tup2), expected_output)

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected_output = []
        self.assertEqual(zip_tuples(test_tup1, test_tup2), expected_output)

    def test_different_length_tuples(self):
        test_tup1 = (1, 2, 3, 4)
        test_tup2 = ('a', 'b')
        expected_output = [(1, 'a'), (2, 'b'), (3, None), (4, None)]
        self.assertEqual(zip_tuples(test_tup1, test_tup2), expected_output)

    def test_single_element_tuples(self):
        test_tup1 = (1,)
        test_tup2 = ('a',)
        expected_output = [(1, 'a')]
        self.assertEqual(zip_tuples(test_tup1, test_tup2), expected_output)

    def test_tuple_with_none(self):
        test_tup1 = (1, None, 3)
        test_tup2 = ('a', 'b', 'c')
        expected_output = [(1, 'a'), (None, 'b'), (3, 'c')]
        self.assertEqual(zip_tuples(test_tup1, test_tup2), expected_output)
