import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(bell_Number(0), 1)
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(3), 4)
        self.assertEqual(bell_Number(4), 10)
        self.assertEqual(bell_Number(5), 20)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(bell_Number(-1), None)
        self.assertEqual(bell_Number(0), 1)
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)
        self.assertEqual(bell_Number(100), 3542248481792619150)

    def test_invalid_inputs(self):
        self.assertIsNone(bell_Number(-1))
        self.assertRaises(TypeError, bell_Number, 'not_a_number')
