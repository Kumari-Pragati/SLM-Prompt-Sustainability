import unittest
from mbpp_962_code import sum_Even

class TestSum_Even(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(sum_Even(1, 5), 6)
        self.assertEqual(sum_Even(2, 5), 9)
        self.assertEqual(sum_Even(3, 5), 9)
        self.assertEqual(sum_Even(4, 5), 9)
        self.assertEqual(sum_Even(5, 5), 5)

    def test_edge_cases(self):
        self.assertEqual(sum_Even(1, 1), 1)
        self.assertEqual(sum_Even(2, 2), 1)
        self.assertEqual(sum_Even(1, 3), 1)
        self.assertEqual(sum_Even(2, 4), 3)
        self.assertEqual(sum_Even(3, 4), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            sum_Even('a', 5)
        with self.assertRaises(TypeError):
            sum_Even(1, 'b')
        with self.assertRaises(TypeError):
            sum_Even(None, 5)
        with self.assertRaises(TypeError):
            sum_Even(1, None)
