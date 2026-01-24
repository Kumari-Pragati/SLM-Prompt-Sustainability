import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(small_nnum([3, 1, 2, 5, 4], 3), [1, 2, 3])

    def test_edge_condition(self):
        self.assertEqual(small_nnum([], 3), [])

    def test_boundary_condition(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 0), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            small_nnum("1, 2, 3, 4, 5", 3)
        with self.assertRaises(TypeError):
            small_nnum([1, 2, 3, 4, 5], "3")
        with self.assertRaises(ValueError):
            small_nnum([1, 2, 3, 4, 5], -1)
