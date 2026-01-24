import unittest
from mbpp_644_code import reverse_Array_Upto_K

class TestReverseArrayUptoK(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 3), [4, 3, 1] + [5, 2, 1])

    def test_edge1(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 1), [3, 2, 1] + [1])

    def test_edge2(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3], 3), [3, 2, 1] + [1, 2, 3])

    def test_edge3(self):
        self.assertEqual(reverse_Array_Upto_K([], 0), [])

    def test_edge4(self):
        self.assertEqual(reverse_Array_Upto_K([1], 1), [1])

    def test_edge5(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 5), [5, 4, 3, 2, 1])

    def test_edge6(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 0), [5, 4, 3, 2, 1])

    def test_edge7(self):
        self.assertEqual(reverse_Array_Upto_K([1, 2, 3, 4, 5], 6), [5, 4, 3, 2, 1])
