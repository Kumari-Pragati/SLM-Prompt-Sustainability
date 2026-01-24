import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):
    def test_lobb_num_typical(self):
        self.assertEqual(lobb_num(1, 1), 1)
        self.assertEqual(lobb_num(2, 1), 2)
        self.assertEqual(lobb_num(3, 2), 3)

    def test_lobb_num_edge(self):
        self.assertEqual(lobb_num(0, 0), 1)
        self.assertEqual(lobb_num(1, 0), 1)
        self.assertEqual(lobb_num(2, 0), 1)

    def test_lobb_num_invalid(self):
        with self.assertRaises(TypeError):
            lobb_num('a', 1)
        with self.assertRaises(TypeError):
            lobb_num(1, 'b')

    def test_lobb_num_boundary(self):
        self.assertEqual(lobb_num(10, 5), 252)
        self.assertEqual(lobb_num(20, 10), 184756)
