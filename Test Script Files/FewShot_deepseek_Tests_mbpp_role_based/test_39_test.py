import unittest
from mbpp_39_code import rearange_string

class TestRearangeString(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(rearange_string('aab'), 'aba')

    def test_edge_case(self):
        self.assertEqual(rearange_string('aaab'), 'aaa')

    def test_boundary_case(self):
        self.assertEqual(rearange_string('aabb'), 'abab')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            rearange_string(123)

    def test_empty_string(self):
        self.assertEqual(rearange_string(''), '')
