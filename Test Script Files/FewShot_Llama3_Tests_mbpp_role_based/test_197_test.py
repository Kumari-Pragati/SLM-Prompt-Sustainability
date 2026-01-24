import unittest
from mbpp_197_code import find_exponentio

class TestFindExponentio(unittest.TestCase):
    def test_typical_use_case(self):
        test_tup1 = (2, 3, 4)
        test_tup2 = (1, 2, 3)
        result = find_exponentio(test_tup1, test_tup2)
        expected_result = (2, 4, 8)
        self.assertEqual(result, expected_result)

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        result = find_exponentio(test_tup1, test_tup2)
        expected_result = ()
        self.assertEqual(result, expected_result)

    def test_single_element_tuples(self):
        test_tup1 = (5,)
        test_tup2 = (2,)
        result = find_exponentio(test_tup1, test_tup2)
        expected_result = (25,)
        self.assertEqual(result, expected_result)

    def test_negative_exponents(self):
        test_tup1 = (2, 3, 4)
        test_tup2 = (-1, -2, -3)
        result = find_exponentio(test_tup1, test_tup2)
        expected_result = (0.5, 0.125, 0.008)
        self.assertAlmostEqual(result, expected_result)
