import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):
    def test_lcm(self):
        self.assertEqual(lcm(2, 3), 6)
        self.assertEqual(lcm(4, 5), 20)
        self.assertEqual(lcm(7, 8), 56)
        self.assertEqual(lcm(9, 10), 90)
        self.assertEqual(lcm(11, 12), 132)
        self.assertEqual(lcm(13, 14), 182)
        self.assertEqual(lcm(15, 16), 240)
        self.assertEqual(lcm(17, 18), 306)
        self.assertEqual(lcm(19, 20), 380)
        self.assertEqual(lcm(21, 22), 462)
        self.assertEqual(lcm(23, 24), 552)
        self.assertEqual(lcm(25, 26), 650)

    def test_lcm_edge_cases(self):
        self.assertEqual(lcm(1, 2), 2)
        self.assertEqual(lcm(2, 1), 2)
        self.assertEqual(lcm(1, 1), 1)
        self.assertEqual(lcm(0, 0), 0)
        self.assertEqual(lcm(0, 1), 1)
        self.assertEqual(lcm(1, 0), 0)

    def test_lcm_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lcm('a', 2)
        with self.assertRaises(TypeError):
            lcm(2, 'b')
        with self.assertRaises(TypeError):
            lcm('a', 'b')
