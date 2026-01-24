import unittest
from mbpp_103_code import eulerian_num

class TestEulerianNum(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(eulerian_num(5, 2), 10)
        self.assertEqual(eulerian_num(3, 1), 3)
        self.assertEqual(eulerian_num(4, 2), 6)

    def test_boundary_cases(self):
        self.assertEqual(eulerian_num(0, 0), 1)
        self.assertEqual(eulerian_num(5, 5), 0)
        self.assertEqual(eulerian_num(0, 1), 0)

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            eulerian_num("5", 2)
        with self.assertRaises(TypeError):
            eulerian_num(5, "2")
        with self.assertRaises(TypeError):
            eulerian_num("5", "2")
        with self.assertRaises(ValueError):
            eulerian_num(-1, 2)
        with self.assertRaises(ValueError):
            eulerian_num(5, -1)
