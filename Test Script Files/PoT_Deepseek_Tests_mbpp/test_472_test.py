import unittest
from mbpp_472_code import check_Consecutive

class TestCheckConsecutive(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(check_Consecutive([1, 2, 3, 4, 5]))
        self.assertTrue(check_Consecutive([10, 9, 8, 7, 6]))
        self.assertTrue(check_Consecutive([1, 3, 5, 7, 9]))

    def test_edge_cases(self):
        self.assertTrue(check_Consecutive([1]))
        self.assertTrue(check_Consecutive([1, 2]))
        self.assertFalse(check_Consecutive([]))

    def test_boundary_conditions(self):
        self.assertTrue(check_Consecutive(list(range(1, 100))))
        self.assertFalse(check_Consecutive(list(range(1, 101))))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_Consecutive(123)
        with self.assertRaises(TypeError):
            check_Consecutive('1,2,3,4,5')
        with self.assertRaises(TypeError):
            check_Consecutive([1, '2', 3, 4, 5])
