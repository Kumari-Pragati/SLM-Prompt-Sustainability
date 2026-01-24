import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(find(10, 2), 5)
        self.assertEqual(find(20, 4), 5)
        self.assertEqual(find(30, 3), 10)

    def test_edge_cases(self):
        self.assertEqual(find(1, 1), 1)
        self.assertEqual(find(0, 1), 0)
        self.assertEqual(find(1, 0), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)
        with self.assertRaises(TypeError):
            find('a', 2)

    def test_boundary_conditions(self):
        self.assertEqual(find(100, 1), 100)
        self.assertEqual(find(-10, 2), -5)
        self.assertEqual(find(0, -1), 0)
