import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup = (1, 2, 3, 4, 5)
        result = add_pairwise(test_tup)
        self.assertEqual(result, (2, 4, 6, 8))

    def test_edge_case_empty_tuple(self):
        test_tup = ()
        with self.assertRaises(IndexError):
            add_pairwise(test_tup)

    def test_edge_case_single_element_tuple(self):
        test_tup = (1,)
        with self.assertRaises(IndexError):
            add_pairwise(test_tup)

    def test_edge_case_tuple_with_one_element(self):
        test_tup = (1, 2)
        result = add_pairwise(test_tup)
        self.assertEqual(result, (3,))

    def test_edge_case_tuple_with_two_elements(self):
        test_tup = (1, 2)
        result = add_pairwise(test_tup)
        self.assertEqual(result, (3,))

    def test_edge_case_tuple_with_three_elements(self):
        test_tup = (1, 2, 3)
        result = add_pairwise(test_tup)
        self.assertEqual(result, (4, 5))
