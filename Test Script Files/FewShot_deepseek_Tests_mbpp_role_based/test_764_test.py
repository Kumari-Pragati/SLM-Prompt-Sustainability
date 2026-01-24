import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(number_ctr('abc123def456'), 6)

    def test_edge_case_empty_string(self):
        self.assertEqual(number_ctr(''), 0)

    def test_boundary_case_only_numbers(self):
        self.assertEqual(number_ctr('1234567890'), 10)

    def test_boundary_case_only_non_numbers(self):
        self.assertEqual(number_ctr('abcdefghijklmnopqrstuvwxyz'), 0)

    def test_typical_use_case_with_mixed_characters(self):
        self.assertEqual(number_ctr('abc123def456ghi789'), 9)

    def test_error_handling_invalid_input(self):
        with self.assertRaises(TypeError):
            number_ctr(1234567890)
