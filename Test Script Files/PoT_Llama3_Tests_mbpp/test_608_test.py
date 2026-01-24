import unittest
from mbpp_608_code import bell_Number

class TestBellNumber(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(bell_Number(3), 2)

    def test_edge_case(self):
        self.assertEqual(bell_Number(1), 1)
        self.assertEqual(bell_Number(2), 2)

    def test_boundary_case(self):
        self.assertEqual(bell_Number(0), 1)
        self.assertEqual(bell_Number(4), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            bell_Number('a')
