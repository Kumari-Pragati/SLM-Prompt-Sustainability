import unittest
from mbpp_453_code import sumofFactors

class TestSumOfFactors(unittest.TestCase):

    def test_sumofFactors_typical(self):
        self.assertEqual(sumofFactors(1), 1)
        self.assertEqual(sumofFactors(2), 1)
        self.assertEqual(sumofFactors(3), 2)
        self.assertEqual(sumofFactors(4), 3)
        self.assertEqual(sumofFactors(5), 4)
        self.assertEqual(sumofFactors(6), 6)
        self.assertEqual(sumofFactors(7), 8)
        self.assertEqual(sumofFactors(8), 15)
        self.assertEqual(sumofFactors(9), 13)
        self.assertEqual(sumofFactors(10), 18)

    def test_sumofFactors_edge(self):
        self.assertEqual(sumofFactors(11), 12)
        self.assertEqual(sumofFactors(12), 28)
        self.assertEqual(sumofFactors(13), 28)
        self.assertEqual(sumofFactors(14), 45)
        self.assertEqual(sumofFactors(15), 60)
        self.assertEqual(sumofFactors(16), 120)
        self.assertEqual(sumofFactors(17), 144)
        self.assertEqual(sumofFactors(18), 216)
        self.assertEqual(sumofFactors(19), 220)
        self.assertEqual(sumofFactors(20), 330)

    def test_sumofFactors_special(self):
        self.assertEqual(sumofFactors(22), 84)
        self.assertEqual(sumofFactors(23), 88)
        self.assertEqual(sumofFactors(24), 300)
        self.assertEqual(sumofFactors(25), 496)
        self.assertEqual(sumofFactors(26), 420)
        self.assertEqual(sumofFactors(27), 576)
        self.assertEqual(sumofFactors(28), 840)
        self.assertEqual(sumofFactors(29), 840)
        self.assertEqual(sumofFactors(30), 1230)

    def test_sumofFactors_invalid(self):
        with self.assertRaises(TypeError):
            sumofFactors("a")
        with self.assertRaises(TypeError):
            sumofFactors(None)
        with self.assertRaises(TypeError):
            sumofFactors(0)
