import unittest
from mbpp_700_code import count_range_in_list

class TestCountRangeInList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 3)

    def test_boundary_conditions(self):
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 1), 1)

    def test_edge_cases(self):
        self.assertEqual(count_range_in_list([], 1, 5), 0)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 6, 10), 0)

    def test_special_cases(self):
        self.assertEqual(count_range_in_list([10, 20, 30, 40, 50], 20, 40), 3)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 2, 4), 3)
        self.assertEqual(count_range_in_list([1, 2, 3, 4, 5], 1, 5), 5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_range_in_list("1, 2, 3, 4, 5", 2, 4)
        with self.assertRaises(TypeError):
            count_range_in_list([1, 2, 3, 4, 5], "2", 4)
        with self.assertRaises(TypeError):
            count_range_in_list([1, 2, 3, 4, 5], 2, "4")
