import unittest
from mbpp_363_code import add_K_element

class TestAddKElements(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = 2
        expected_result = [(3, 4, 5), (6, 7, 8)]
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_empty_list(self):
        test_list = []
        K = 2
        expected_result = []
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_single_element_list(self):
        test_list = [[1]]
        K = 2
        expected_result = [(3,)]
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_negative_K(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = -2
        expected_result = [(0, 1, 2), (2, 3, 4)]
        self.assertEqual(add_K_element(test_list, K), expected_result)

    def test_large_K(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = 100
        expected_result = [(101, 102, 103), (104, 105, 106)]
        self.assertEqual(add_K_element(test_list, K), expected_result)
