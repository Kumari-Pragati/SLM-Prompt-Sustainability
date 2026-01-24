import unittest
from mbpp_21_code import multiples_of_num

class TestMultiplesOfNum(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(multiples_of_num(3, 10), [10, 20, 30])
        self.assertEqual(multiples_of_num(5, 20), [20, 40, 60, 80, 100, 120, 140, 160, 180, 200])

    def test_edge_conditions(self):
        self.assertEqual(multiples_of_num(1, 10), [10])
        self.assertEqual(multiples_of_num(0, 10), [])
        self.assertEqual(multiples_of_num(10, 0), [])

    def test_boundary_conditions(self):
        self.assertEqual(multiples_of_num(10, 100), list(range(100, 1000, 10)))
        self.assertEqual(multiples_of_num(1, 1000), list(range(100, 1100, 10)))

    def test_complex_cases(self):
        self.assertEqual(multiples_of_num(2, 20), [20, 40])
        self.assertEqual(multiples_of_num(3, 30), [30, 60, 90])
