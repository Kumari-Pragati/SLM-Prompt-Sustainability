import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (0, 1, 2)
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, (1, 1, 1))

    def test_edge_case_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, ())

    def test_edge_case_single_element_tuples(self):
        test_tup1 = (5,)
        test_tup2 = (3,)
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, (2,))

    def test_edge_case_tuples_of_different_lengths(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5)
        with self.assertRaises(IndexError):
            substract_elements(test_tup1, test_tup2)

    def test_invalid_input_type(self):
        test_tup1 = [1, 2, 3]
        test_tup2 = (4, 5)
        with self.assertRaises(TypeError):
            substract_elements(test_tup1, test_tup2)
