import unittest
from mbpp_841_code import get_inv_count

class TestGetInvCount(unittest.TestCase):

    def test_get_inv_count(self):
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5), 4)
        self.assertEqual(get_inv_count([1, 3, 2, 4, 5], 5), 2)
        self.assertEqual(get_inv_count([5, 1, 3, 2, 4], 5, 1), 3)
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5, 1), 0)
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5, 1), 4)
        self.assertEqual(get_inv_count([1, 3, 2, 4, 5], 5, 1), 2)
        self.assertEqual(get_inv_count([5, 1, 3, 2, 4], 5, 2), 3)
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5, 2), 0)
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5, 2), 4)
        self.assertEqual(get_inv_count([1, 3, 2, 4, 5], 5, 2), 2)
        self.assertEqual(get_inv_count([5, 1, 3, 2, 4], 5, 3), 3)
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5, 3), 0)
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5, 3), 4)
        self.assertEqual(get_inv_count([1, 3, 2, 4, 5], 5, 3), 2)
        self.assertEqual(get_inv_count([5, 1, 3, 2, 4], 5, 4), 3)
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5, 4), 0)
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5, 4), 4)
        self.assertEqual(get_inv_count([1, 3, 2, 4, 5], 5, 4), 2)
        self.assertEqual(get_inv_count([5, 1, 3, 2, 4], 5, 5), 3)
        self.assertEqual(get_inv_count([1, 2, 3, 4, 5], 5, 5), 0)
        self.assertEqual(get_inv_count([5, 4, 3, 2, 1], 5, 5), 4)
        self.assertEqual(get_inv_count([1, 3, 2, 4, 5], 5, 5), 2)
