import unittest
from mbpp_363_code import add_K_element

class TestAddKElements(unittest.TestCase):

    def test_simple_addition(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = 2
        expected_output = [(3, 4, 5), (6, 7, 8)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_empty_list(self):
        test_list = []
        K = 2
        expected_output = []
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_negative_K(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = -2
        expected_output = [(0, 1, 2), (2, 3, 4)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_large_K(self):
        test_list = [[1, 2, 3], [4, 5, 6]]
        K = 100
        expected_output = [(101, 102, 103), (104, 105, 106)]
        self.assertEqual(add_K_element(test_list, K), expected_output)

    def test_large_list(self):
        test_list = [[i for i in range(1, 1001)]]
        K = 100
        expected_output = [[i+100 for i in range(1, 1001)]]
        self.assertEqual(add_K_element(test_list, K), expected_output)
