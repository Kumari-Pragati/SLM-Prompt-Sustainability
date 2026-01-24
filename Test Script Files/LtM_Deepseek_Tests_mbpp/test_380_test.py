import unittest
from mbpp_380_code import multi_list

class TestMultiList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(multi_list(1, 1), [[0]])
        self.assertEqual(multi_list(2, 2), [[0, 0], [0, 1]])

    def test_edge_conditions(self):
        self.assertEqual(multi_list(0, 0), [])
        self.assertEqual(multi_list(1, 0), [[]])
        self.assertEqual(multi_list(0, 1), [])

    def test_boundary_conditions(self):
        self.assertEqual(multi_list(100, 100), [[i*j for j in range(100)] for i in range(100)])

    def test_complex_cases(self):
        self.assertEqual(multi_list(3, 4), [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6]])
