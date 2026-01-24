import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_greater((1, 2, 3), (4, 5, 6)))

    def test_edge_case_equal_elements(self):
        self.assertFalse(check_greater((1, 2, 3), (1, 2, 3)))

    def test_edge_case_second_tuple_shorter(self):
        self.assertFalse(check_greater((1, 2, 3), (1, 2)))

    def test_edge_case_first_tuple_shorter(self):
        self.assertTrue(check_greater((1, 2), (1, 2, 3)))

    def test_edge_case_empty_tuples(self):
        self.assertTrue(check_greater((), ()))

    def test_error_case_non_tuple_input(self):
        with self.assertRaises(TypeError):
            check_greater((1, 2, 3), "not a tuple")

    def test_error_case_tuple_with_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            check_greater((1, 2, '3'), (1, 2, 3))
