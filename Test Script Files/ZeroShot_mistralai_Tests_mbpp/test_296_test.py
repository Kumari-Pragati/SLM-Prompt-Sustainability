import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(get_Inv_Count([], 0), 0)

    def test_single_element_list(self):
        self.assertEqual(get_Inv_Count([1], 1), 0)

    def test_increasing_list(self):
        self.assertEqual(get_Inv_Count([1, 2, 3], 3), 0)

    def test_decreasing_list(self):
        self.assertEqual(get_Inv_Count([3, 2, 1], 3), 2)

    def test_mixed_list(self):
        self.assertEqual(get_Inv_Count([2, 1, 3, 5, 4], 5), 3)
