import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 1), "EVEN")
        self.assertEqual(check_last([1, 3, 5, 7, 9], 5, 1), "ODD")

    def test_edge_cases(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 1), "EVEN")
        self.assertEqual(check_last([1, 3, 5, 7, 9], 5, 1), "ODD")
        self.assertEqual(check_last([1, 1, 1, 1, 1], 5, 1), "EVEN")
        self.assertEqual(check_last([1, 1, 1, 1, 2], 5, 1), "ODD")

    def test_boundary_cases(self):
        self.assertEqual(check_last([1, 1, 1, 1, 1], 5, 1), "EVEN")
        self.assertEqual(check_last([1, 1, 1, 1, 2], 5, 1), "ODD")
        self.assertEqual(check_last([1, 1, 1, 2, 2], 5, 1), "ODD")
        self.assertEqual(check_last([1, 1, 1, 2, 3], 5, 1), "ODD")

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            check_last(1, 2, 3)
        with self.assertRaises(TypeError):
            check_last([1, 2, 3], 'a', 3)
        with self.assertRaises(TypeError):
            check_last([1, 2, 3], 2, 'a')
