import unittest
from mbpp_614_code import cummulative_sum

class TestCummulativeSum(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(cummulative_sum([[1], [2], [3]]), 6)
        self.assertEqual(cummulative_sum([[-1], [-2], [-3]]), 6)
        self.assertEqual(cummulative_sum([[0], [0], [0]]), 0)

    def test_edge_cases(self):
        self.assertEqual(cummulative_sum([[]]), 0)
        self.assertEqual(cummulative_sum([[1]]), 1)
        self.assertEqual(cummulative_sum([[1], [2]]), 3)
        self.assertEqual(cummulative_sum([[1], [2], [3], [4]]), 10)

    def test_empty_sublists(self):
        self.assertEqual(cummulative_sum([[1, 2], [], [3]]), 6)
        self.assertEqual(cummulative_sum([[], [1, 2], [3]]), 3)
        self.assertEqual(cummulative_sum([[], [], [3]]), 3)

    def test_mixed_types(self):
        self.assertRaises(TypeError, cummulative_sum, [1, 'a', [2]])
        self.assertRaises(TypeError, cummulative_sum, [['a'], [2], [3]])
        self.assertRaises(TypeError, cummulative_sum, [1, 2, 'a'])
