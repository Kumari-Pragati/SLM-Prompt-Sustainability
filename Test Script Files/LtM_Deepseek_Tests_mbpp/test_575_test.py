import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_no(2, 3, 1, 10), 6)
        self.assertEqual(count_no(3, 2, 1, 10), 4)

    def test_boundary_conditions(self):
        self.assertEqual(count_no(1, 1, 1, 1), 1)
        self.assertEqual(count_no(10, 10, 1, 100), 100)

    def test_edge_conditions(self):
        self.assertEqual(count_no(1, 0, 1, 10), 1)
        self.assertEqual(count_no(1, 11, 1, 10), 10)
        self.assertEqual(count_no(1, 1, 10, 20), 11)
        self.assertEqual(count_no(1, 1, 100, 101), 101)

    def test_complex_cases(self):
        self.assertEqual(count_no(3, 2, 10, 30), 18)
        self.assertEqual(count_no(5, 3, 20, 50), 40)
