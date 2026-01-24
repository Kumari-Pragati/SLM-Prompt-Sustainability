import unittest
from mbpp_726_code import multiply_elements

class TestMultiplyElements(unittest.TestCase):

    def test_normal_input(self):
        self.assertTupleEqual(multiply_elements((1, 2, 3, 4)), (2, 3, 6))
        self.assertTupleEqual(multiply_elements((5, 6, 7, 8)), (10, 12, 14))

    def test_edge_and_boundary_conditions(self):
        self.assertTupleEqual(multiply_elements((1)), ())
        self.assertTupleEqual(multiply_elements((1, 2)), (2,))
        self.assertTupleEqual(multiply_elements((1, 2, 3)), (2, 3))
        self.assertTupleEqual(multiply_elements((1, 2, 3, 4, 5)), (2, 3, 4, 6, 5))

    def test_special_cases(self):
        self.assertTupleEqual(multiply_elements((0, 1, 2)), (0, 0, 2))
        self.assertTupleEqual(multiply_elements((-1, 1, 2)), (-1, 1, 2))
        self.assertTupleEqual(multiply_elements((1, -1, 2)), (1, -1, 2))
