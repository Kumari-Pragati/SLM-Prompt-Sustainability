import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(bell_Number(0), 1)
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(3), 4)
        self.assertEqual(bell_Number(4), 10)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(bell_Number(-1), None)
        self.assertEqual(bell_Number(5), 15)
        self.assertEqual(bell_Number(10), 220)
        self.assertEqual(bell_Number(20), 102729375)

    def test_complex_scenarios(self):
        self.assertEqual(bell_Number(100), 3542248481792619150)
