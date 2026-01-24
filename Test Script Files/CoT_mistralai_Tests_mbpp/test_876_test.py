import unittest
from mbpp_876_code import lcm

class TestLcm(unittest.TestCase):
    def test_lcm_positive(self):
        self.assertEqual(lcm(2, 4), 4)
        self.assertEqual(lcm(8, 16), 16)
        self.assertEqual(lcm(30, 40), 120)

    def test_lcm_zero(self):
        self.assertEqual(lcm(0, 4), 0)
        self.assertEqual(lcm(4, 0), 0)

    def test_lcm_one(self):
        self.assertEqual(lcm(1, 2), 2)
        self.assertEqual(lcm(2, 1), 2)

    def test_lcm_negative(self):
        self.assertEqual(lcm(-2, 4), 4)
        self.assertEqual(lcm(4, -2), 4)

    def test_lcm_large_numbers(self):
        self.assertEqual(lcm(123456789, 987654321), 2367616577)

    def test_lcm_same_number(self):
        for x in [1, 2, 3, 4, 5, 10, 25]:
            self.assertEqual(lcm(x, x), x)

    def test_lcm_invalid_input(self):
        self.assertRaises(TypeError, lcm, "string", 4)
        self.assertRaises(TypeError, lcm, 4, "string")
        self.assertRaises(TypeError, lcm, [1, 2, 3], 4)
        self.assertRaises(TypeError, lcm, 4, [1, 2, 3])
