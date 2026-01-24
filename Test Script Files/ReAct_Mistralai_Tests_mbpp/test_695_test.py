import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertFalse(check_greater((1, 2, 3), (2, 3, 4)))
        self.assertFalse(check_greater((3, 2, 1), (2, 3, 4)))
        self.assertFalse(check_greater((2, 3, 4), (1, 2, 3)))

    def test_edge_case_equal_elements(self):
        self.assertTrue(check_greater((1, 1, 2), (1, 1, 2)))
        self.assertTrue(check_greater((1, 2, 1), (1, 2, 1)))
        self.assertTrue(check_greater((2, 1, 1), (2, 1, 1)))

    def test_edge_case_single_element(self):
        self.assertTrue(check_greater((1), (2)))
        self.assertFalse(check_greater((2), (1)))

    def test_edge_case_empty_tuples(self):
        self.assertTrue(check_greater((), (1)))
        self.assertTrue(check_greater((1), ()))

    def test_error_case_different_lengths(self):
        with self.assertRaises(ValueError):
            check_greater((1, 2, 3), (1, 2))
        with self.assertRaises(ValueError):
            check_greater((1, 2), (1, 2, 3))
