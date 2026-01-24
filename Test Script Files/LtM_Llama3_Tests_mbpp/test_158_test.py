import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 3), 1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 5), 0)

    def test_edge(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 0), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 6), -1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 0, 2), -1)

    def test_complex(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5, 6], 6, 2), 2)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5, 6, 7], 7, 3), 1)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5, 6, 7, 8], 8, 4), 0)
