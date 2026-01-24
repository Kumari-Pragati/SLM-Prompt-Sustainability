import unittest
from mbpp_126_code import sum

class TestSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(sum(10, 20), 10)

    def test_boundary_conditions(self):
        self.assertEqual(sum(1, 1), 1)
        self.assertEqual(sum(0, 0), 0)

    def test_edge_cases(self):
        self.assertEqual(sum(1, 2), 1)
        self.assertEqual(sum(2, 1), 1)
        self.assertEqual(sum(1, 100), 1)
        self.assertEqual(sum(100, 1), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum("10", 20)
        with self.assertRaises(TypeError):
            sum(10, "20")
        with self.assertRaises(TypeError):
            sum("10", "20")
