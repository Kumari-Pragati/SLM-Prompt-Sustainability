import unittest
from mbpp_555_code import difference

class TestDifferenceFunction(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 2)
        self.assertEqual(difference(3), 6)
        self.assertEqual(difference(4), 12)
        self.assertEqual(difference(5), 20)

    def test_edge_cases(self):
        self.assertEqual(difference(0), 0)
        self.assertEqual(difference(-1), 0)
        self.assertEqual(difference(1e6), 499500500500)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            difference('a')
        with self.assertRaises(TypeError):
            difference(None)
