import unittest
from mbpp_126_code import sum

class TestSumFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum(12, 18), 6)

    def test_typical_case_2(self):
        self.assertEqual(sum(25, 50), 25)

    def test_boundary_case(self):
        self.assertEqual(sum(1, 1), 1)

    def test_edge_case(self):
        self.assertEqual(sum(0, 0), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            sum("12", 18)

    def test_negative_numbers(self):
        self.assertEqual(sum(-12, -18), 0)
