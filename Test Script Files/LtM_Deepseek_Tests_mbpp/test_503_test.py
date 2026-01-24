import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4]), [2, 1])

    def test_edge_conditions(self):
        self.assertEqual(add_consecutive_nums([1]), [])
        self.assertEqual(add_consecutive_nums([]), [])

    def test_complex_cases(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [2, 1, 2])
        self.assertEqual(add_consecutive_nums([10, 20, 30, 40]), [10, 10])
