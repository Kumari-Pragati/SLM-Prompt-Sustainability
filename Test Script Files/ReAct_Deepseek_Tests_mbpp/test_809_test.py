import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (0, 1, 2)))

    def test_edge_case_equal_elements(self):
        self.assertFalse(check_smaller((1, 2, 3), (1, 2, 3)))

    def test_edge_case_second_tuple_longer(self):
        self.assertFalse(check_smaller((1, 2), (1, 2, 3)))

    def test_edge_case_first_tuple_longer(self):
        self.assertFalse(check_smaller((1, 2, 3), (1, 2)))

    def test_error_case_non_tuple_input(self):
        with self.assertRaises(TypeError):
            check_smaller((1, 2, 3), [1, 2, 3])

    def test_error_case_empty_tuple(self):
        self.assertTrue(check_smaller((), ()))
