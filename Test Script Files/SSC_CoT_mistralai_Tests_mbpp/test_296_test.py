import unittest
from mbpp_296_code import get_Inv_Count

class TestGetInvCount(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(get_Inv_Count([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(get_Inv_Count([5, 4, 3, 2, 1], 5), 5)
        self.assertEqual(get_Inv_Count([1, 1, 1, 1, 1], 5), 0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(get_Inv_Count([1, 2, 2, 1], 4), 1)
        self.assertEqual(get_Inv_Count([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 10), 45)
        self.assertEqual(get_Inv_Count([], 0), 0)
        self.assertEqual(get_Inv_Count([1], 1), 0)

    def test_negative_numbers(self):
        self.assertEqual(get_Inv_Count([-1, 2, -3, 4], 4), 3)
        self.assertEqual(get_Inv_Count([-5, -4, -3, -2, -1], 5), 10)

    def test_duplicate_numbers(self):
        self.assertEqual(get_Inv_Count([1, 1, 2, 2, 3], 5), 2)
        self.assertEqual(get_Inv_Count([1, 1, 1, 1, 1], 5), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            get_Inv_Count(1, 'string')
        with self.assertRaises(ValueError):
            get_Inv_Count('list', 5)
