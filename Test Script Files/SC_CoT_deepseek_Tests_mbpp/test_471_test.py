import unittest

from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_typical_case(self):
        arr = [10, 20, 30]
        lens = len(arr)
        n = 7
        self.assertEqual(find_remainder(arr, lens, n), 6)

    def test_edge_case(self):
        arr = [0, 0, 0]
        lens = len(arr)
        n = 1
        self.assertEqual(find_remainder(arr, lens, n), 0)

    def test_boundary_case(self):
        arr = [10**9, 20**9, 30**9]
        lens = len(arr)
        n = 10**9
        self.assertEqual(find_remainder(arr, lens, n), 0)

    def test_special_case(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        lens = len(arr)
        n = 2
        self.assertEqual(find_remainder(arr, lens, n), 0)

    def test_invalid_input(self):
        arr = [10, 20, 30]
        lens = len(arr)
        n = 0
        with self.assertRaises(ZeroDivisionError):
            find_remainder(arr, lens, n)
