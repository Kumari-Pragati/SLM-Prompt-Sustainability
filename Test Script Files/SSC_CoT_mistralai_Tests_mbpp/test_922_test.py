import unittest
from mbpp_922_code import max_product

class TestMaxProduct(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_product([1, 2, 3, 4, 5]), (1, 5))
        self.assertEqual(max_product([-1, -2, -3, -4, -5]), (-1, -5))
        self.assertEqual(max_product([0, 0]), None)

    def test_edge_cases(self):
        self.assertEqual(max_product([1]), (1, 1))
        self.assertEqual(max_product([1, 0]), (1, 0))
        self.assertEqual(max_product([0, 1]), (0, 1))
        self.assertEqual(max_product([-1, 1]), (-1, 1))
        self.assertEqual(max_product([1, -1]), (1, -1))

    def test_negative_numbers(self):
        self.assertEqual(max_product([-2, -3, 4]), (-2, 4))
        self.assertEqual(max_product([-2, -3, -4]), (-2, -4))

    def test_empty_list(self):
        self.assertIsNone(max_product([]))

    def test_single_element(self):
        self.assertIsNone(max_product([1]))
        self.assertIsNone(max_product([-1]))
        self.assertIsNone(max_product([0]))
