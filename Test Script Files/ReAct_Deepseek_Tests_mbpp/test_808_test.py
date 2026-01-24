import unittest
from mbpp_808_code import check_K

class TestCheckK(unittest.TestCase):

    def test_typical_case(self):
        test_tup = (1, 2, 3, 4, 5)
        K = 3
        self.assertTrue(check_K(test_tup, K))

    def test_typical_case_not_present(self):
        test_tup = (1, 2, 3, 4, 5)
        K = 6
        self.assertFalse(check_K(test_tup, K))

    def test_empty_tuple(self):
        test_tup = ()
        K = 1
        self.assertFalse(check_K(test_tup, K))

    def test_single_element_tuple(self):
        test_tup = (1,)
        K = 1
        self.assertTrue(check_K(test_tup, K))
        K = 2
        self.assertFalse(check_K(test_tup, K))

    def test_negative_numbers(self):
        test_tup = (-1, -2, -3, -4, -5)
        K = -3
        self.assertTrue(check_K(test_tup, K))

    def test_large_numbers(self):
        test_tup = (1000, 2000, 3000, 4000, 5000)
        K = 3000
        self.assertTrue(check_K(test_tup, K))

    def test_large_tuple(self):
        test_tup = tuple(range(1, 10001))
        K = 5000
        self.assertTrue(check_K(test_tup, K))
