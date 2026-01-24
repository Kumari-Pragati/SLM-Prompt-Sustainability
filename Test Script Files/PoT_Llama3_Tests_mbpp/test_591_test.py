import unittest
from mbpp_591_code import swap_List

class TestSwapList(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(swap_List([1, 2, 3, 4, 5]), [5, 2, 3, 4, 1])

    def test_edge(self):
        self.assertEqual(swap_List([1]), [1])
        self.assertEqual(swap_List([1, 2]), [2, 1])

    def test_boundary(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 2, 1])
        self.assertEqual(swap_List([1, 2, 3, 4]), [4, 2, 3, 1])

    def test_invalid(self):
        with self.assertRaises(TypeError):
            swap_List()
