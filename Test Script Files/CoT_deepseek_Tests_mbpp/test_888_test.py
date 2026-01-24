import unittest
from mbpp_888_code import substract_elements

class TestSubstractElements(unittest.TestCase):

    def test_typical_case(self):
        test_tup1 = ((10, 20, 30), (40, 50, 60))
        test_tup2 = ((5, 10, 15), (20, 25, 30))
        expected_output = ((5, 10, 15), (20, 25, 30))
        self.assertEqual(substract_elements(test_tup1, test_tup2), expected_output)

    def test_empty_tuples(self):
        test_tup1 = ()
        test_tup2 = ()
        expected_output = ()
        self.assertEqual(substract_elements(test_tup1, test_tup2), expected_output)

    def test_single_element_tuples(self):
        test_tup1 = (10,)
        test_tup2 = (5,)
        expected_output = (5,)
        self.assertEqual(substract_elements(test_tup1, test_tup2), expected_output)

    def test_different_length_tuples(self):
        test_tup1 = (10, 20, 30, 40)
        test_tup2 = (5, 10)
        with self.assertRaises(ValueError):
            substract_elements(test_tup1, test_tup2)

    def test_negative_numbers(self):
        test_tup1 = (10, 20, 30)
        test_tup2 = (20, 30, 40)
        expected_output = (-10, -10, -10)
        self.assertEqual(substract_elements(test_tup1, test_tup2), expected_output)
