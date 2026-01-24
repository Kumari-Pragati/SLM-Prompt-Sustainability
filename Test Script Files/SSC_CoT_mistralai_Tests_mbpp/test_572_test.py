import unittest
from mbpp_572_code import two_unique_nums

class TestTwoUniqueNums(unittest.TestCase):
    def test_typical_input(self):
        self.assertListEqual(two_unique_nums([1, 2, 3, 4, 5]), [1, 3, 5])

    def test_edge_case_single_unique(self):
        self.assertListEqual(two_unique_nums([1, 1, 2]), [2])

    def test_edge_case_no_unique(self):
        self.assertListEqual(two_unique_nums([1, 1, 1, 2]), [])

    def test_edge_case_single_element(self):
        self.assertListEqual(two_unique_nums([1]), [])

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            two_unique_nums([])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            two_unique_nums("1,2,3")
