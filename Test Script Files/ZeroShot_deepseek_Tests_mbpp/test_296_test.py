import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):

    def test_get_Inv_Count(self):
        self.assertEqual(get_Inv_Count([1, 20, 6, 4, 5], 5), 5)
        self.assertEqual(get_Inv_Count([1, 3, 5, 2, 4, 6], 6), 3)
        self.assertEqual(get_Inv_Count([10, 20, 30, 40, 50], 5), 0)
        self.assertEqual(get_Inv_Count([5, 4, 3, 2, 1], 5), 10)
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5], 5), 0)
