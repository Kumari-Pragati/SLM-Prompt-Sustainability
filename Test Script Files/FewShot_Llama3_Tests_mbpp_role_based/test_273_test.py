import unittest
from mbpp_273_code import substract_elements

class TestSubstractElements(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = (10, 5, 3)
        test_tup2 = (5, 2, 1)
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, (5, 3, 2))

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, ())

    def test_tuples_of_different_lengths(self):
        test_tup1 = (1, 2, 3, 4)
        test_tup2 = (5, 6)
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, (1-5, 2-6, 3, 4))

    def test_tuples_with_negative_numbers(self):
        test_tup1 = (-5, 2, 3)
        test_tup2 = (2, -1, 1)
        result = substract_elements(test_tup1, test_tup2)
        self.assertEqual(result, (-7, 3, 2))
