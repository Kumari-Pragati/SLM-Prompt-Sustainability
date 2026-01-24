import unittest
from mbpp_259_code import maximize_elements

class TestMaximizeElements(unittest.TestCase):

    def test_typical_case(self):
        test_tup1 = ((1, 2, 3), (4, 5, 6))
        test_tup2 = ((7, 8, 9), (10, 11, 12))
        expected_result = ((7, 8, 9), (10, 11, 12))
        self.assertEqual(maximize_elements(test_tup1, test_tup2), expected_result)

    def test_edge_case_different_lengths(self):
        test_tup1 = ((1, 2, 3), (4, 5))
        test_tup2 = ((7, 8, 9), (10, 11, 12, 13))
        expected_result = ((7, 8, 9), (10, 11, 12, 13))
        self.assertEqual(maximize_elements(test_tup1, test_tup2), expected_result)

    def test_edge_case_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected_result = ()
        self.assertEqual(maximize_elements(test_tup1, test_tup2), expected_result)

    def test_error_case_mismatched_tuple_lengths(self):
        test_tup1 = ((1, 2, 3), (4, 5))
        test_tup2 = ((7, 8), (10, 11, 12))
        with self.assertRaises(ValueError):
            maximize_elements(test_tup1, test_tup2)
