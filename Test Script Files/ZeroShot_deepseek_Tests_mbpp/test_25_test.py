import unittest
from mbpp_25_code import find_Product

class TestFindProduct(unittest.TestCase):

    def test_find_Product(self):
        self.assertEqual(find_Product([2, 3, 4, 5, 6], 5), 720)
        self.assertEqual(find_Product([1, 2, 3, 4, 5], 5), 120)
        self.assertEqual(find_Product([1, 1, 1, 1, 1], 5), 1)
        self.assertEqual(find_Product([10, 20, 30, 40, 50], 5), 12000000)
        self.assertEqual(find_Product([-1, -2, -3, -4, -5], 5), -120)
