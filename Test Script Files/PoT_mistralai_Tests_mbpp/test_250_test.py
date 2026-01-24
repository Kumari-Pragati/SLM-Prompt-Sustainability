import unittest
from mbpp_250_code import count_X

class TestCountX(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(count_X((1, 2, 'x', 'x', 'y'), 'x'), 2)

    def test_empty_list(self):
        self.assertEqual(count_X([], 'x'), 0)

    def test_single_element(self):
        self.assertEqual(count_X([1], 'x'), 0)

    def test_single_element_as_x(self):
        self.assertEqual(count_X([1], 1), 1)

    def test_boundary_case_first_element(self):
        self.assertEqual(count_X([1, 'x'], 'x'), 1)

    def test_boundary_case_last_element(self):
        self.assertEqual(count_X(['x', 1], 'x'), 1)

    def test_boundary_case_only_x(self):
        self.assertEqual(count_X(['x'], 'x'), 1)

    def test_boundary_case_only_non_x(self):
        self.assertEqual(count_X([1], 1), 1)
