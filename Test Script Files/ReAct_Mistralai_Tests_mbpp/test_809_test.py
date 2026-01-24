import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (0, 1, 2)))

    def test_edge_case_equal_elements(self):
        self.assertFalse(check_smaller((1, 1, 2), (1, 1, 2)))

    def test_edge_case_reversed_order(self):
        self.assertFalse(check_smaller((1, 2, 3), (3, 2, 1)))

    def test_edge_case_empty_tuples(self):
        self.assertIsNone(check_smaller((), ()))

    def test_edge_case_single_element(self):
        self.assertTrue(check_smaller((1), (0)))
        self.assertFalse(check_smaller((0), (1)))

    def test_error_case_non_tuple_input(self):
        with self.assertRaises(TypeError):
            check_smaller(1, 2)
