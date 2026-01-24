import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)

    def test_boundary_conditions(self):
        self.assertEqual(catalan_number(10), 16796)
        self.assertEqual(catalan_number(20), 109418989131512359209)

    def test_invalid_inputs(self):
        with self.assertRaises(Exception):
            catalan_number(-1)
        with self.assertRaises(Exception):
            catalan_number(1.5)
        with self.assertRaises(Exception):
            catalan_number('a')
