import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(multi_list(3, 4), [[0, 0, 0, 3], [0, 1, 2, 6], [0, 2, 4, 8], [3, 6, 8, 9]])

    def test_edge_cases(self):
        self.assertEqual(multi_list(0, 0), [])
        self.assertEqual(multi_list(1, 1), [[0]])
        self.assertEqual(multi_list(1, 0), [[]])
        self.assertEqual(multi_list(0, 1), [[]])

    def test_boundary_cases(self):
        self.assertEqual(multi_list(1, 2), [[0, 0], [1, 2]])
        self.assertEqual(multi_list(2, 1), [[0, 1], [2, 0]])

    def test_negative_inputs(self):
        with self.assertRaises(ValueError):
            multi_list(-1, 2)
        with self.assertRaises(ValueError):
            multi_list(1, -1)
