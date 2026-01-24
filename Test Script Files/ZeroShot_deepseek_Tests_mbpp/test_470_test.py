import unittest
from mbpp_470_code import add_pairwise

class TestAddPairwise(unittest.TestCase):

    def test_add_pairwise(self):
        self.assertEqual(add_pairwise((1, 2, 3, 4, 5)), (3, 5, 7, 9))
        self.assertEqual(add_pairwise((10, 20, 30, 40, 50)), (30, 60, 90, 130))
        self.assertEqual(add_pairwise((0, 0, 0, 0, 0)), (0, 0, 0, 0))
        self.assertEqual(add_pairwise((1,)), ())
        self.assertEqual(add_pairwise(()), ())
