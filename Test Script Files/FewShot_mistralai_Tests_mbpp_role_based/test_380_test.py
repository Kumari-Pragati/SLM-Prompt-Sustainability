import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_typical_use_case(self):
        result = multi_list(3, 4)
        self.assertEqual(result, [[0, 0, 0, 1], [0, 0, 2, 3], [0, 3, 4, 6]])

    def test_edge_case_zero_row(self):
        with self.assertRaises(ValueError):
            multi_list(0, 4)

    def test_edge_case_zero_col(self):
        with self.assertRaises(ValueError):
            multi_list(3, 0)
