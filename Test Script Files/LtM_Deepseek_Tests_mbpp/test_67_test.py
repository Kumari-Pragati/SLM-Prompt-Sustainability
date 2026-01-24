import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)
        self.assertEqual(bell_number(3), 5)

    def test_edge_conditions(self):
        self.assertEqual(bell_number(0), 0)
        self.assertEqual(bell_number(1), 1)

    def test_complex_cases(self):
        self.assertEqual(bell_number(4), 15)
        self.assertEqual(bell_number(5), 52)
