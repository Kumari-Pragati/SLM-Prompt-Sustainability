import unittest
from mbpp_126_code import sum

class TestSumFunction(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(sum(10, 20), 10)
        self.assertEqual(sum(21, 21), 21)
        self.assertEqual(sum(100, 50), 50)

    def test_edge_cases(self):
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(1, 1), 1)

    def test_boundary_cases(self):
        self.assertEqual(sum(1000000000, 2000000000), 1000000000)
        self.assertEqual(sum(1, 2), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum("10", 20)
        with self.assertRaises(TypeError):
            sum(10, "20")
        with self.assertRaises(TypeError):
            sum("10", "20")
