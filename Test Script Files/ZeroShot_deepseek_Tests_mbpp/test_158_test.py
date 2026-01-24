import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_min_Ops(self):
        self.assertEqual(min_Ops([1, 1, 1], 3, 2), 1)
        self.assertEqual(min_Ops([1, 2, 3], 3, 2), -1)
        self.assertEqual(min_Ops([10, 10, 10], 3, 10), 3)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 7)
        self.assertEqual(min_Ops([10, 20, 30, 40, 50], 5, 10), 5)
