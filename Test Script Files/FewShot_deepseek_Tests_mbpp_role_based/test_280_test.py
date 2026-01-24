import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):
    def test_typical_use_case(self):
        data_list = [1, 2, 3, 4, 5]
        item = 3
        self.assertTrue(sequential_search(data_list, item))

    def test_edge_condition(self):
        data_list = []
        item = 3
        self.assertFalse(sequential_search(data_list, item))

    def test_boundary_condition(self):
        data_list = [1]
        item = 1
        self.assertTrue(sequential_search(data_list, item))

    def test_invalid_input(self):
        data_list = [1, 2, 3, 4, 5]
        item = 'a'
        with self.assertRaises(TypeError):
            sequential_search(data_list, item)
