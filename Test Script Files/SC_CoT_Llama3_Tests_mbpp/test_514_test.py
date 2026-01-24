import unittest
from mbpp_514_code import sum_elements

class TestSumElements(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(sum_elements((1, 2, 3)), 6)

    def test_edge_case_empty(self):
        self.assertEqual(sum_elements(()), 0)

    def test_edge_case_single(self):
        self.assertEqual(sum_elements((5)), 5)

    def test_edge_case_negative(self):
        self.assertEqual(sum_elements((-1, 2, 3)), -1 + 2 + 3)

    def test_edge_case_mixed(self):
        self.assertEqual(sum_elements((-1, 2, 3, 4)), -1 + 2 + 3 + 4)

    def test_invalid_input_non_tuple(self):
        with self.assertRaises(TypeError):
            sum_elements(123)

    def test_invalid_input_non_iterable(self):
        with self.assertRaises(TypeError):
            sum_elements("hello")
