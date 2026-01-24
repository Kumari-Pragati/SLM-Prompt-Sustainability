import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)
        self.assertEqual(catalan_number(5), 42)

    def test_boundary_cases(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(30), 16789838878572471)

    def test_edge_cases(self):
        self.assertEqual(catalan_number(-1), 1)
        self.assertEqual(catalan_number(-10), 1)
        self.assertEqual(catalan_number(31), 16789838878572471)
        self.assertEqual(catalan_number(32), 16789838878572471)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            catalan_number("5")
        with self.assertRaises(TypeError):
            catalan_number(None)
        with self.assertRaises(TypeError):
            catalan_number([1, 2, 3])
