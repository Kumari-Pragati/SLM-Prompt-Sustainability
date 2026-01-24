import unittest
from mbpp_912_code import lobb_num

class TestLobbNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(lobb_num(3, 2), 10.0)
        self.assertEqual(lobb_num(4, 3), 35.0)
        self.assertEqual(lobb_num(5, 4), 105.0)

    def test_edge_cases(self):
        self.assertEqual(lobb_num(0, 0), 1.0)
        self.assertEqual(lobb_num(1, 0), 2.0)
        self.assertEqual(lobb_num(0, 1), 1.0)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            lobb_num("3", 2)
        with self.assertRaises(TypeError):
            lobb_num(3, "2")
        with self.assertRaises(ValueError):
            lobb_num(-1, 2)
        with self.assertRaises(ValueError):
            lobb_num(3, -2)
