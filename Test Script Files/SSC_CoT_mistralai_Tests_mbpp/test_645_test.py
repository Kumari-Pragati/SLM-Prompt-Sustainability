import unittest
from mbpp_645_code import range
from six.moves import zip_longest

from645_code import find_k_product

class TestFindKProduct(unittest.TestCase):

    def test_normal_input(self):
        data = [
            ([[1, 2, 3], [4, 5, 6]], 1),
            ([[7, 8, 9], [10, 11, 12]], 2),
            ([[13, 14, 15], [16, 17, 18]], 0),
        ]
        for test_list, k in data:
            self.assertEqual(find_k_product(test_list, k), get_product([sub[k] for sub in test_list]))

    def test_edge_and_boundary_conditions(self):
        data = [
            ([[1], [2]], 1),
            ([[1], [2]], 2),
            ([[1], [2]], 3),
            ([[1], [2]], 0),
            ([[1], []], 0),
            ([[1]], 0),
        ]
        for test_list, k in data:
            self.assertEqual(find_k_product(test_list, k), get_product([sub[k] for sub in test_list]))

    def test_invalid_input(self):
        data = [
            ([[1], [2]], -1),
            ([[1], [2]], 4),
        ]
        for test_list, k in data:
            with self.assertRaises(IndexError):
                find_k_product(test_list, k)
