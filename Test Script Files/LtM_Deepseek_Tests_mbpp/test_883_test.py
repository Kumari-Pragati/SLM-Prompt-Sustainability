import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(div_of_nums([10, 20, 30, 40], 2, 5), [20, 40])
        self.assertEqual(div_of_nums([15, 30, 45, 60], 3, 5), [30, 45, 60])

    def test_edge_conditions(self):
        self.assertEqual(div_of_nums([], 2, 3), [])
        self.assertEqual(div_of_nums([10, 20, 30, 40], 1, 2), [20, 40])
        self.assertEqual(div_of_nums([10, 20, 30, 40], 20, 5), [20, 40])
        self.assertEqual(div_of_nums([10, 20, 30, 40], 2, 40), [20, 40])

    def test_complex_cases(self):
        self.assertEqual(div_of_nums([100, 200, 300, 400], 20, 5), [200, 400])
        self.assertEqual(div_of_nums([10, 20, 30, 40], 10, 2), [])
