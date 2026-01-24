import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):

    def test_get_inv_count(self):
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5], 5), 0)
        self.assertEqual(get_Inv_Count([5, 4, 3, 2, 1], 5), 4)
        self.assertEqual(get_Inv_Count([1, 3, 2, 4, 5], 5), 2)
        self.assertEqual(get_Inv_Count([5, 1, 2, 3, 4], 5), 4)
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5, 6], 6, ), 0)
        self.assertEqual(get_Inv_Count([5, 4, 3, 2, 1, 6], 6), 4)
        self.assertEqual(get_Inv_Count([1, 3, 2, 4, 5, 6], 6), 2)
        self.assertEqual(get_Inv_Count([5, 1, 2, 3, 4, 6], 6), 4)
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5, 6, 7], 7), 0)
        self.assertEqual(get_Inv_Count([7, 6, 5, 4, 3, 2, 1], 7), 6)
        self.assertEqual(get_Inv_Count([1, 3, 2, 4, 5, 6, 7], 7), 3)
        self.assertEqual(get_Inv_Count([5, 1, 2, 3, 4, 6, 7], 7), 4)
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5, 6, 7, 8], 8), 0)
        self.assertEqual(get_Inv_Count([8, 7, 6, 5, 4, 3, 2, 1], 8), 7)
        self.assertEqual(get_Inv_Count([1, 3, 2, 4, 5, 6, 7, 8], 8), 3)
        self.assertEqual(get_Inv_Count([5, 1, 2, 3, 4, 6, 7, 8], 8), 4)
