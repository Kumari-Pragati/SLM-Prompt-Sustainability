import unittest
from mbpp_401_code import add_nested_tuples

class TestAddNestedTuples(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = ((1, 2), (3, 4))
        test_tup2 = ((5, 6), (7, 8))
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), ((6, 8), (10, 12)))

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), ())

    def test_tuples_of_diff_lengths(self):
        test_tup1 = ((1, 2), (3, 4))
        test_tup2 = ((5, 6))
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), ((6, 8),))

    def test_tuples_with_single_elements(self):
        test_tup1 = ((1,))
        test_tup2 = ((2,))
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), ((3,)))

    def test_tuples_with_negative_numbers(self):
        test_tup1 = ((-1, 2), (3, -4))
        test_tup2 = ((5, 6), (7, 8))
        self.assertEqual(add_nested_tuples(test_tup1, test_tup2), ((4, 8), (10, 4)))
