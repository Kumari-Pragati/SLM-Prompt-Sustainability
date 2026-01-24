import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (2, 1, 0)))
        self.assertTrue(check_smaller((5, 4, 3), (6, 5, 4)))

    def test_edge_case_equal_elements(self):
        self.assertTrue(check_smaller((1, 1, 2), (1, 1, 2)))

    def test_edge_case_reverse_order(self):
        self.assertTrue(check_smaller((2, 1, 0), (2, 1, 3)))

    def test_edge_case_empty_tuples(self):
        self.assertFalse(check_smaller((), (1, 2, 3)))
        self.assertFalse(check_smaller((1, 2, 3), ()))

    def test_invalid_input_different_lengths(self):
        self.assertRaises(ValueError, check_smaller, (1, 2, 3), (1, 2))
