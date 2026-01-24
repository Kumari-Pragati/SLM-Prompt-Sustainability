import unittest
from mbpp_360_code import get_carol

class TestGetCarol(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(get_carol(1), 0)
        self.assertEqual(get_carol(2), 3)
        self.assertEqual(get_carol(3), 35)

    def test_edge_cases(self):
        self.assertEqual(get_carol(0), 0)
        self.assertEqual(get_carol(4), 115)

    def test_negative_inputs(self):
        with self.assertRaises(TypeError):
            get_carol(-1)

    def test_non_integer_inputs(self):
        with self.assertRaises(TypeError):
            get_carol(1.5)

    def test_large_inputs(self):
        self.assertEqual(get_carol(10), 5764801)

    def test_zero_inputs(self):
        self.assertEqual(get_carol(0), 0)
