import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_typical_input(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5, 6)
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, (-3, -3, -3))

    def test_edge_case_zero(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (0, 0, 0)
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, (1, 2, 3))

    def test_edge_case_negative(self):
        test_tup1 = (-1, -2, -3)
        test_tup2 = (-4, -5, -6)
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, (3, 3, 3))

    def test_edge_case_single_element(self):
        test_tup1 = (1,)
        test_tup2 = (2,)
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, (-1,))

    def test_edge_case_empty(self):
        test_tup1 = ()
        test_tup2 = ()
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, ())

    def test_edge_case_mismatched_lengths(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = (4, 5)
        with self.assertRaises(IndexError):
            substract_elements(test_tup1, test_tup2)

    def test_edge_case_mismatched_types(self):
        test_tup1 = (1, 2, 3)
        test_tup2 = ['a', 'b', 'c']
        with self.assertRaises(TypeError):
            substract_elements(test_tup1, test_tup2)
