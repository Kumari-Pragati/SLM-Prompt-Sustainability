import unittest
from mbpp_363_code import add_K_element

class TestAddKElements(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = 2
        expected_output = [(3, 4, 5), (6, 7, 8)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_edge_condition(self):
        test_list = [[0, 0, 0], [-1, -1, -1]]
        K = 0
        expected_output = [(0, 0, 0), (-1, -1, -1)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_boundary_condition(self):
        test_list = [[1000, 2000, 3000], [-1000, -2000, -3000]]
        K = 10000
        expected_output = [(11000, 21000, 31000), (-9000, -19000, -29000)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_invalid_input(self):
        test_list = "invalid_input"
        K = 2
        with self.assertRaises(TypeError):
            add_K_element(test_list, K)
