import unittest
from mbpp_689_code import min_jumps

class TestMinJumps(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 3)

    def test_boundary_case(self):
        arr = [0]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 0)

    def test_edge_case(self):
        arr = [2, 3, 1, 1, 4]
        n = len(arr)
        self.assertEqual(min_jumps(arr, n), 2)

    def test_invalid_input(self):
        arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
        n = -1
        with self.assertRaises(ValueError):
            min_jumps(arr, n)
