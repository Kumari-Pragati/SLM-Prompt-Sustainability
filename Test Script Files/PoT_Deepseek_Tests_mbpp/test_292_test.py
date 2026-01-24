import unittest
from mbpp_292_code import find

class TestFindFunction(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find(10, 2), 5)
        self.assertEqual(find(15, 3), 5)
        self.assertEqual(find(20, 4), 5)

    def test_edge_cases(self):
        self.assertEqual(find(0, 1), 0)
        self.assertEqual(find(1, 1), 1)

    def test_boundary_conditions(self):
        self.assertEqual(find(292, 1), 292)
        self.assertEqual(find(1, 292), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find("10", 2)
        with self.assertRaises(TypeError):
            find(10, "2")
        with self.assertRaises(ZeroDivisionError):
            find(10, 0)
