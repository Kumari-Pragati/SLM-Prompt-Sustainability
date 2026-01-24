import unittest
from mbpp_618_code import div_list

class TestDivList(unittest.TestCase):

    def test_typical_case(self):
        self.assertAlmostEqual(div_list([10, 20, 30], [1, 2, 3]), [10, 10, 10])

    def test_edge_case_zero(self):
        self.assertAlmostEqual(div_list([10, 20, 30], [0, 2, 3]), [float('inf'), 10, 10])

    def test_boundary_case_empty_lists(self):
        self.assertEqual(div_list([], []), [])

    def test_corner_case_single_element(self):
        self.assertAlmostEqual(div_list([10], [2]), [5])

    def test_invalid_input_different_lengths(self):
        with self.assertRaises(ValueError):
            div_list([10, 20, 30], [1, 2])

    def test_invalid_input_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div_list([10, 20, 30], [0, 2, 0])
