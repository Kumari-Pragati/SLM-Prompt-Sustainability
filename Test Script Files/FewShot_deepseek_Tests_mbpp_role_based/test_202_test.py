import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove_even('abcdefg'), 'bdf')

    def test_edge_condition(self):
        self.assertEqual(remove_even('a'), '')

    def test_boundary_condition(self):
        self.assertEqual(remove_even(''), '')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_even(12345)
