import unittest
from mbpp_502_code import find

class TestFindFunction(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(5, 2), 1)
        self.assertEqual(find(7, 3), 1)
        self.assertEqual(find(0, 5), 0)

    def test_edge_cases(self):
        self.assertEqual(find(-5, 3), -2)
        self.assertEqual(find(10, 0), 10)
        self.assertEqual(find(0, 0), 0)
        self.assertEqual(find(-10, -5), -10)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find("a", 3)
        with self.assertRaises(TypeError):
            find(10, "b")
