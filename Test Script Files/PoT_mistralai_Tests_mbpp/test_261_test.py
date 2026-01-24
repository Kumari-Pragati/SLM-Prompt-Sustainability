import unittest
from mbpp_261_code import division_elements

class TestDivisionElements(unittest.TestCase):

    def test_typical_case(self):
        self.assertTupleEqual(division_elements((3, 5, 7), (2, 2, 3)), (1, 2, 1))
        self.assertTupleEqual(division_elements((10, 2, 5), (2, 5, 1)), (5, 0, 5))

    def test_edge_case_zero(self):
        self.assertRaises(ZeroDivisionError, lambda: division_elements((0, 1), (1,)))
        self.assertRaises(ZeroDivisionError, lambda: division_elements((1, 0), ()))

    def test_edge_case_negative(self):
        self.assertTupleEqual(division_elements((-3, -5, -7), (-2, -2, -3)), (1, 2, 1))
        self.assertTupleEqual(division_elements((-10, -2, -5), (-2, -5, -1)), (-5, 1, -5))

    def test_empty_input(self):
        self.assertRaises(ValueError, lambda: division_elements((), ()))
        self.assertRaises(ValueError, lambda: division_elements((1, 2, 3), ()))
        self.assertRaises(ValueError, lambda: division_elements((), (1, 2, 3)))
