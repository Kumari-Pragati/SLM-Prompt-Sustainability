import unittest
from mbpp_158_code import min_Ops

class TestMinOps(unittest.TestCase):

    def test_min_Ops_valid_input(self):
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 2), 2)
        self.assertEqual(min_Ops([10, 20, 30, 40, 50], 5, 5), 5)
        self.assertEqual(min_Ops([1, 2, 3, 4, 5], 5, 1), -1)

    def test_min_Ops_invalid_input(self):
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3, 4, 5], '5', 2)
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3, 4, 5], 5, '2')
        with self.assertRaises(TypeError):
            min_Ops([1, 2, 3, 4, 5], '5', '2')

    def test_min_Ops_edge_cases(self):
        self.assertEqual(min_Ops([1], 1, 2), 0)
        self.assertEqual(min_Ops([10], 1, 5), 2)
        self.assertEqual(min_Ops([], 0, 2), -1)
