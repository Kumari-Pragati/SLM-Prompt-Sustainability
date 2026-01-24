import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4, 6])

    def test_edge_conditions(self):
        self.assertEqual(div_of_nums([], 2, 3), [])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 0, 3), [3, 4, 5])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 0), [2, 3, 4, 5])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 1, 1), [1, 2, 3, 4, 5])

    def test_complex_cases(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 5, 10), [10, 20, 30, 40, 50])
        self.assertEqual(div_of_nums([1, 2, 3, 4, 5], 2, 3), [2, 3, 4, 6])
        self.assertEqual(div_of_nums([10, 20, 30, 40, 50], 15, 20), [30, 60])
