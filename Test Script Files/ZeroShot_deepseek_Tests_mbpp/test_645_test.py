import unittest
from mbpp_645_code import find_k_product

class TestFindKProduct(unittest.TestCase):

    def test_find_k_product(self):
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1), 40)
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2), 120)
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0), 252)
        self.assertEqual(find_k_product([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3), 360)
