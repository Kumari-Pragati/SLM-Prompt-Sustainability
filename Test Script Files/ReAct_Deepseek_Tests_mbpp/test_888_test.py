import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_case(self):
        test_tup1 = ((10, 20, 30), (40, 50, 60))
        test_tup2 = ((5, 10, 15), (20, 25, 30))
        expected_result = ((5, 10, 15), (20, 25, 30))
        self.assertEqual(substract_elements(test_tup1, test_tup2), expected_result)

    def test_edge_case_zero(self):
        test_tup1 = ((0, 0, 0), (0, 0, 0))
        test_tup2 = ((5, 10, 15), (20, 25, 30))
        expected_result = ((-5, -10, -15), (-20, -25, -30))
        self.assertEqual(substract_elements(test_tup1, test_tup2), expected_result)

    def test_edge_case_negative(self):
        test_tup1 = ((10, 20, 30), (40, 50, 60))
        test_tup2 = ((-5, -10, -15), (-20, -25, -30))
        expected_result = ((15, 30, 45), (60, 75, 90))
        self.assertEqual(substract_elements(test_tup1, test_tup2), expected_result)

    def test_error_case_different_lengths(self):
        test_tup1 = ((10, 20, 30), (40, 50, 60, 70))
        test_tup2 = ((5, 10, 15), (20, 25, 30))
        with self.assertRaises(ValueError):
            substract_elements(test_tup1, test_tup2)
