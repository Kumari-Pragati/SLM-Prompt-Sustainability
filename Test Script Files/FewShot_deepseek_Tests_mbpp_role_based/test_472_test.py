import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))

    def test_edge_condition(self):
        self.assertTrue(check_Consecutive([5, 4, 3, 2, 1]))

    def test_boundary_condition(self):
        self.assertTrue(check_Consecutive([0, 1, 2, 3, 4, 5, 6]))
        self.assertFalse(check_Consecutive([1, 2, 4, 5, 6]))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_Consecutive("1, 2, 3, 4, 5")
        with self.assertRaises(TypeError):
            check_Consecutive([1, 2, "3", 4, 5])
