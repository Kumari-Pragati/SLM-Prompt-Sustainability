import unittest
from mbpp_363_code import add_K_element

class TestAddKElement(unittest.TestCase):
    def test_typical_input(self):
        test_list = [(1, 2), (3, 4)]
        K = 5
        result = add_K_element(test_list, K)
        self.assertEqual(result, [(6, 7), (8, 9)])

    def test_edge_case(self):
        test_list = [(1, 2), (3, 4)]
        K = 0
        result = add_K_element(test_list, K)
        self.assertEqual(result, [(1, 2), (3, 4)])

    def test_edge_case_negative(self):
        test_list = [(1, 2), (3, 4)]
        K = -1
        result = add_K_element(test_list, K)
        self.assertEqual(result, [(-1, 1), (2, 3)])

    def test_edge_case_single_element(self):
        test_list = [(1, 2)]
        K = 3
        result = add_K_element(test_list, K)
        self.assertEqual(result, [(4, 5)])

    def test_edge_case_empty_list(self):
        test_list = []
        K = 5
        result = add_K_element(test_list, K)
        self.assertEqual(result, [])

    def test_invalid_input_non_integer(self):
        test_list = [(1, 2), (3, 4)]
        K = 'five'
        with self.assertRaises(TypeError):
            add_K_element(test_list, K)

    def test_invalid_input_non_list(self):
        test_list = None
        K = 5
        with self.assertRaises(TypeError):
            add_K_element(test_list, K)
