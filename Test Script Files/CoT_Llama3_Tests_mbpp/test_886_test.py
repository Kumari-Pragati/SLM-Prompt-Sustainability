import unittest
from mbpp_886_code import sum_num

class TestSumNum(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(sum_num([1, 2, 3, 4, 5]), 3.0)

    def test_edge_case_single_element(self):
        self.assertEqual(sum_num([1]), 1.0)

    def test_edge_case_zero_elements(self):
        self.assertEqual(sum_num([]), 0.0)

    def test_edge_case_single_zero(self):
        self.assertEqual(sum_num([0]), 0.0)

    def test_edge_case_single_non_numeric(self):
        with self.assertRaises(TypeError):
            sum_num(['a'])

    def test_edge_case_multiple_non_numeric(self):
        with self.assertRaises(TypeError):
            sum_num(['a', 'b', 'c'])

    def test_edge_case_mixed_types(self):
        with self.assertRaises(TypeError):
            sum_num([1, 'a', 3, 4])
