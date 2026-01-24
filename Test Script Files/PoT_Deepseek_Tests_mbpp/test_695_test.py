import unittest
from mbpp_695_code import check_greater

class TestCheckGreater(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_greater((1, 2, 3), (4, 5, 6)))

    def test_edge_case_equal_elements(self):
        self.assertFalse(check_greater((1, 2, 3), (1, 2, 3)))

    def test_boundary_case_empty_tuples(self):
        self.assertTrue(check_greater((), ()))

    def test_corner_case_one_element(self):
        self.assertTrue(check_greater((1,), (2,)))
        self.assertFalse(check_greater((2,), (1,)))

    def test_corner_case_negative_numbers(self):
        self.assertTrue(check_greater((-1, -2, -3), (-4, -5, -6)))
        self.assertFalse(check_greater((-1, -2, -3), (-1, -2, -3)))

    def test_corner_case_mixed_types(self):
        with self.assertRaises(TypeError):
            check_greater((1, 'a'), (2, 'b'))
