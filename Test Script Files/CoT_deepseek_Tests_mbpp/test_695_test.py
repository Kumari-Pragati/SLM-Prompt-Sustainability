import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_greater((1, 2, 3), (4, 5, 6)))

    def test_reverse_order(self):
        self.assertFalse(check_greater((4, 5, 6), (1, 2, 3)))

    def test_equal_tuples(self):
        self.assertFalse(check_greater((1, 2, 3), (1, 2, 3)))

    def test_different_lengths(self):
        self.assertFalse(check_greater((1, 2), (1, 2, 3)))

    def test_negative_numbers(self):
        self.assertTrue(check_greater((-1, -2, -3), (0, 1, 2)))

    def test_empty_tuples(self):
        self.assertTrue(check_greater((), (1, 2, 3)))

    def test_single_element_tuples(self):
        self.assertTrue(check_greater((1,), (2,)))

    def test_large_numbers(self):
        self.assertTrue(check_greater((10**6, 10**6), (2*10**6, 2*10**6)))

    def test_float_numbers(self):
        self.assertTrue(check_greater((1.1, 2.2, 3.3), (4.4, 5.5, 6.6)))
