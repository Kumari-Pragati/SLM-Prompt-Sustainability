import unittest
from mbpp_200_code import position_max

class TestPositionMax(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(position_max([1, 2, 3, 4, 5]), [4])

    def test_edge_case_single_max_value(self):
        self.assertEqual(position_max([1, 1, 1, 1, 1]), [0, 1, 2, 3, 4])

    def test_boundary_case_empty_list(self):
        self.assertEqual(position_max([]), [])

    def test_boundary_case_list_with_one_element(self):
        self.assertEqual(position_max([1]), [0])

    def test_error_handling_non_list_input(self):
        with self.assertRaises(TypeError):
            position_max("1,2,3,4,5")

    def test_error_handling_list_with_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            position_max([1, "2", 3, 4, 5])
