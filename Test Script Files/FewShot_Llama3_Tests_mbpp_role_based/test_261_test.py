import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = (10, 2, 5, 3)
        test_tup2 = (2, 1, 2, 1)
        self.assertEqual(division_elements(test_tup1, test_tup2), (5, 5, 2, 3))

    def test_zero_division(self):
        test_tup1 = (10, 0, 5, 3)
        test_tup2 = (2, 1, 2, 1)
        with self.assertRaises(ZeroDivisionError):
            division_elements(test_tup1, test_tup2)

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        self.assertEqual(division_elements(test_tup1, test_tup2), ())

    def test_single_element_tuples(self):
        test_tup1 = (10,)
        test_tup2 = (2,)
        self.assertEqual(division_elements(test_tup1, test_tup2), (5,))

    def test_tuple_with_single_zero(self):
        test_tup1 = (10, 2, 5, 0, 3)
        test_tup2 = (2, 1, 2, 1, 1)
        with self.assertRaises(ZeroDivisionError):
            division_elements(test_tup1, test_tup2)
