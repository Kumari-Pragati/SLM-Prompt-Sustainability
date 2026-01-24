import unittest
from mbpp_460_code import Extract

class TestExtract(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Extract([('a', 1), ('b', 2), ('c', 3)]), ['a', 'b', 'c'])

    def test_edge_condition(self):
        self.assertEqual(Extract([]), [])

    def test_boundary_condition(self):
        self.assertEqual(Extract([('a', 1)]), ['a'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Extract(123)
