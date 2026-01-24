import unittest
from mbpp_429_code import and_tuples

class TestAndTuples(unittest.TestCase):

    def test_and_tuples_typical_case(self):
        test_tup1 = (1, 2, 3, 4)
        test_tup2 = (1, 2, 5, 6)
        expected_result = (1, 2)
        self.assertTupleEqual(and_tuples(test_tup1, test_tup2), expected_result)

    def test_and_tuples_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected_result = ()
        self.assertTupleEqual(and_tuples(test_tup1, test_tup2), expected_result)

    def test_and_tuples_single_element_tuples(self):
        test_tup1 = (1,)
        test_tup2 = (1,)
        expected_result = (1,)
        self.assertTupleEqual(and_tuples(test_tup1, test_tup2), expected_result)

    def test_and_tuples_different_lengths(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (1, 2, 3, 4)
        expected_result = (1, 2)
        self.assertTupleEqual(and_tuples(test_tup1, test_tup2), expected_result)

    def test_and_tuples_negative_numbers(self):
        test_tup1 = (-1, 0, 1)
        test_tup2 = (-1, 2, 3)
        expected_result = (-1,)
        self.assertTupleEqual(and_tuples(test_tup1, test_tup2), expected_result)

    def test_and_tuples_floats(self):
        test_tup1 = (1.0, 2.0, 3.0)
        test_tup2 = (1.0, 2.0, 4.0)
        expected_result = (1.0, 2.0)
        self.assertTupleEqual(and_tuples(test_tup1, test_tup2), expected_result)

    def test_and_tuples_strings(self):
        test_tup1 = ('a', 'b', 'c')
        test_tup2 = ('a', 'd', 'e')
        expected_result = ()
        self.assertTupleEqual(and_tuples(test_tup1, test_tup2), expected_result)

    def test_and_tuples_error_case_non_iterable(self):
        with self.assertRaises(TypeError):
            and_tuples('string', test_tup2)
