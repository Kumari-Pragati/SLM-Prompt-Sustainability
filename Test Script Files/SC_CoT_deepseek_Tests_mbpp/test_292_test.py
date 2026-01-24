import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find(10, 2), 5)

    def test_boundary_case(self):
        self.assertEqual(find(0, 1), 0)
        self.assertEqual(find(1, 1), 1)

    def test_edge_case(self):
        self.assertEqual(find(2, 1), 2)
        self.assertEqual(find(10, 20), 0)

    def test_negative_numbers(self):
        self.assertEqual(find(-10, 2), -5)
        self.assertEqual(find(10, -2), -5)
        self.assertEqual(find(-10, -2), 5)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find("10", 2)
        with self.assertRaises(TypeError):
            find(10, "2")
        with self.assertRaises(TypeError):
            find("10", "2")
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)
