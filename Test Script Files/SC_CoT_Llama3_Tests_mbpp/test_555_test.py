import unittest
from mbpp_555_code import difference

class TestDifferenceFunction(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 1)
        self.assertEqual(difference(3), 3)
        self.assertEqual(difference(4), 6)
        self.assertEqual(difference(5), 10)

    def test_edge_cases(self):
        self.assertEqual(difference(-1), 0)
        self.assertEqual(difference(0), 0)
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 1)
        self.assertEqual(difference(3), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            difference("a")
        with self.assertRaises(TypeError):
            difference(None)

    def test_large_inputs(self):
        self.assertEqual(difference(100), 5050)
        self.assertEqual(difference(200), 20100)
