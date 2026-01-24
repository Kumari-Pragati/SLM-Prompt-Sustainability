import unittest

from mbpp_363_code import add_K_element

class TestAddKElements(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = 2
        expected_output = [(3, 4, 5), (6, 7, 8)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_edge_case(self):
        test_list = [[0, 0, 0], [-1, -1, -1]]
        K = 0
        expected_output = [(0, 0, 0), (-1, -1, -1)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_boundary_case(self):
        test_list = [[-100, 0, 100], [0, 50, 100]]
        K = 50
        expected_output = [(-50, 50, 150), (50, 100, 150)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_corner_case(self):
        test_list = [[(10**6), (10**6), (10**6)], [-(10**6), -(10**6), -(10**6)]]
        K = 10**6
        expected_output = [(2*(10**6)), (2*(10**6)), (2*(10**6))], [(0), (-2*(10**6)), (-2*(10**6))]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_invalid_input(self):
        test_list = "invalid_input"
        K = 2
        with self.assertRaises(TypeError):
            add_K_element(test_list, K)
