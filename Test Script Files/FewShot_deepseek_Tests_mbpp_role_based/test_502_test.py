import unittest
from mbpp_502_code import find

class TestFind(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find(10, 3), 1)

    def test_boundary_conditions(self):
        self.assertEqual(find(0, 5), 0)
        self.assertEqual(find(10, 1), 0)

    def test_edge_cases(self):
        self.assertEqual(find(10, 0), None)
        self.assertEqual(find(0, 0), None)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find('10', 3)
        with self.assertRaises(TypeError):
            find(10, '3')
        with self.assertRaises(TypeError):
            find('10', '3')
