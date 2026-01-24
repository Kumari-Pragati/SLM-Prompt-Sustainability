import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(lobb_num(1, 1), 1)
        self.assertEqual(lobb_num(2, 1), 1)
        self.assertEqual(lobb_num(1, 2), 1)
        self.assertEqual(lobb_num(2, 2), 2)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(lobb_num(0, 0), 1)
        self.assertEqual(lobb_num(0, 1), 1)
        self.assertEqual(lobb_num(1, 0), 1)
        self.assertEqual(lobb_num(1, 1), 1)
        self.assertEqual(lobb_num(2, 0), 1)
        self.assertEqual(lobb_num(2, 1), 1)
        self.assertEqual(lobb_num(2, 2), 2)
        self.assertEqual(lobb_num(0, 2), 1)
        self.assertEqual(lobb_num(1, 2), 1)
        self.assertEqual(lobb_num(2, 2), 2)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lobb_num('a', 1)
        with self.assertRaises(TypeError):
            lobb_num(1, 'b')
        with self.assertRaises(TypeError):
            lobb_num('a', 'b')
