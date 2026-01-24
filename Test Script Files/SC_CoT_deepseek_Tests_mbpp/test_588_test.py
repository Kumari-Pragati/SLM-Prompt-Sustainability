import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(big_diff([1, 2, 3]), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(big_diff([1]), 0)

    def test_edge_case_same_elements(self):
        self.assertEqual(big_diff([1, 1, 1]), 0)

    def test_boundary_case_max_min(self):
        self.assertEqual(big_diff([-1000000, 1000000]), 2000000)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(TypeError):
            big_diff([])

    def test_invalid_input_non_list(self):
        with self.assertRaises(TypeError):
            big_diff("1, 2, 3")

    def test_invalid_input_non_integer_elements(self):
        with self.assertRaises(TypeError):
            big_diff([1, 2.5, 3])
