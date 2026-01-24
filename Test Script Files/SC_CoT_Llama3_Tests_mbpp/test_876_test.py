import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(10, 15), 30)
        self.assertEqual(lcm(20, 25), 100)

    def test_edge_cases(self):
        self.assertEqual(lcm(1, 2), 2)
        self.assertEqual(lcm(2, 3), 6)
        self.assertEqual(lcm(5, 10), 10)

    def test_larger_numbers(self):
        self.assertEqual(lcm(100, 200), 200)
        self.assertEqual(lcm(500, 600), 600)
        self.assertEqual(lcm(1000, 2000), 2000)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            lcm("a", 5)
        with self.assertRaises(TypeError):
            lcm(5, "b")
