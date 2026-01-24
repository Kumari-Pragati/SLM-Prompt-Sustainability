import unittest
from mbpp_27_code import remove

class TestRemove(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(remove(['abc123', 'def456']), ['abc', 'def'])

    def test_edge_condition(self):
        self.assertEqual(remove(['1234567890']), [''])

    def test_boundary_condition(self):
        self.assertEqual(remove(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']), ['', '', '', '', '', '', '', '', '', ''])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove(123456)
