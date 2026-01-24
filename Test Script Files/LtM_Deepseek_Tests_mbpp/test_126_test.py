import unittest
from mbpp_126_code import sum

class TestSumFunction(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(sum(2, 3), 1)
        self.assertEqual(sum(10, 5), 5)

    def test_boundary_conditions(self):
        self.assertEqual(sum(1, 1), 1)
        self.assertEqual(sum(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(sum(1, 2), 1)
        self.assertEqual(sum(2, 1), 1)
        self.assertEqual(sum(0, 2), 0)
        self.assertEqual(sum(2, 0), 0)
        self.assertEqual(sum(0, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum("2", 3)
        with self.assertRaises(TypeError):
            sum(2, "3")
        with self.assertRaises(TypeError):
            sum("2", "3")
