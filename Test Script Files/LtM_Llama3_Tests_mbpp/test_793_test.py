import unittest
from mbpp_793_code import last

class TestLastFunction(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 3, 5), 2)
        self.assertEqual(last([10, 20, 30, 40, 50], 30, 5), 4)
        self.assertEqual(last([1, 2, 3, 4, 5], 5, 5), 4)

    def test_edge_cases(self):
        self.assertEqual(last([], 10, 0), -1)
        self.assertEqual(last([10], 10, 1), 0)
        self.assertEqual(last([10, 20, 30, 40, 50], 50, 5), 4)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            last(None, 10, 5)
        with self.assertRaises(TypeError):
            last([1, 2, 3, 4, 5], None, 5)
        with self.assertRaises(TypeError):
            last([1, 2, 3, 4, 5], 10, None)
