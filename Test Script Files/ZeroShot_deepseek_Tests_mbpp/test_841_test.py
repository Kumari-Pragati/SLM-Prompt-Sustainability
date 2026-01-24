import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_get_inv_count(self):
        self.assertEqual(get_inv_count([1, 20, 6, 4, 5], 5), 5)
        self.assertEqual(get_inv_count([1, 3, 5, 2, 4, 6], 6), 3)
        self.assertEqual(get_inv_count([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10), 45)
        self.assertEqual(get_inv_count([1, 1, 1, 1, 1], 5), 0)
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5), 10)
