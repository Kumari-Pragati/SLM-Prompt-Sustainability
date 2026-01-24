import unittest
from mbpp_67_code import bell_number

class TestBellNumber(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(bell_number(3), 5)

    def test_edge_case(self):
        self.assertEqual(bell_number(1), 1)
        self.assertEqual(bell_number(2), 2)

    def test_boundary_case(self):
        self.assertEqual(bell_number(0), 1)
        self.assertEqual(bell_number(4), 15)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            bell_number('a')
