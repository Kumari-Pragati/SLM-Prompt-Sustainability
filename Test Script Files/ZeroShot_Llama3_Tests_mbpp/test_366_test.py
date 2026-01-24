import unittest
from mbpp_366_code import adjacent_num_product

class TestAdjacentNumProduct(unittest.TestCase):

    def test_adjacent_num_product(self):
        self.assertEqual(adjacent_num_product([1, 2, 3, 4]), 6)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4]), 2)
        self.assertEqual(adjacent_num_product([5, 5, 5, 5]), 25)
        self.assertEqual(adjacent_num_product([-5, -5, -5, -5]), 25)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5]), 6)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5]), 2)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6]), 12)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5, -6]), 12)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7]), 42)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5, -6, -7]), 42)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8]), 56)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5, -6, -7, -8]), 56)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8, 9]), 72)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5, -6, -7, -8, -9]), 72)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 90)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), 90)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 110)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]), 110)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 132)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]), 132)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]), 156)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13]), 156)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]), 182)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14]), 182)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 210)
        self.assertEqual(adjacent_num_product([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]), 210)
        self.assertEqual(adjacent_num_product([1, 2, 3, 4, 5, 6,