import unittest
from mbpp_502_code import find

class TestFindFunction(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(15, 5), 0)
        self.assertEqual(find(20, 4), 0)

    def test_edge_cases(self):
        self.assertEqual(find(0, 3), 0)
        self.assertEqual(find(3, 0), 3)
        self.assertEqual(find(-10, 3), -1)
        self.assertEqual(find(10, -3), 1)

    def test_negative_inputs(self):
        self.assertEqual(find(-10, 3), -1)
        self.assertEqual(find(-15, 5), -0)
        self.assertEqual(find(-20, 4), -0)

    def test_zero_inputs(self):
        self.assertEqual(find(0, 0), 0)
        self.assertEqual(find(0, 3), 0)
        self.assertEqual(find(3, 0), 3)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find("a", 3)
        with self.assertRaises(TypeError):
            find(10, "b")
