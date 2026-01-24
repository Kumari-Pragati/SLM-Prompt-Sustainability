import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_smaller((5, 3), (4, 2)))

    def test_edge_case_equal_elements(self):
        self.assertFalse(check_smaller((3, 3), (4, 4)))

    def test_boundary_case_second_tuple_shorter(self):
        self.assertFalse(check_smaller((4, 5, 6), (1, 2)))

    def test_boundary_case_first_tuple_shorter(self):
        self.assertTrue(check_smaller((1, 2), (4, 5, 6)))

    def test_corner_case_empty_tuples(self):
        self.assertTrue(check_smaller((), ()))

    def test_corner_case_one_element_tuples(self):
        self.assertFalse(check_smaller((5,), (4,)))

    def test_corner_case_same_elements(self):
        self.assertFalse(check_smaller((3, 3, 3), (3, 3, 3)))
