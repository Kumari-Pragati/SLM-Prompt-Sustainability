import unittest
from mbpp_62_code import smallest_num

class TestSmallestNum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(smallest_num([5, 3, 9, 1]), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(smallest_num([5]), 5)

    def test_boundary_case_empty_list(self):
        with self.assertRaises(ValueError):
            smallest_num([])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            smallest_num("1, 2, 3")

    def test_invalid_input_list_with_non_numeric(self):
        with self.assertRaises(TypeError):
            smallest_num([1, "2", 3])
