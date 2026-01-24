import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(multi_list(3, 4), [[0, 0, 0, 3], [0, 1, 2, 6], [0, 2, 4, 8], [3, 6, 8, 9]])

    def test_edge_case_zero(self):
        self.assertEqual(multi_list(0, 3), [])

    def test_edge_case_one(self):
        self.assertEqual(multi_list(1, 3), [[0, 0, 1]])

    def test_edge_case_negative(self):
        self.assertRaises(ValueError, multi_list, -1, 3)
        self.assertRaises(ValueError, multi_list, 1, -1)
