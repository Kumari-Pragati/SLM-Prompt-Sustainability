import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 2)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 2)
        self.assertEqual(count_Fac(6), 3)
        self.assertEqual(count_Fac(7), 2)
        self.assertEqual(count_Fac(8), 3)
        self.assertEqual(count_Fac(9), 3)
        self.assertEqual(count_Fac(10), 2)

    def test_edge(self):
        self.assertEqual(count_Fac(0), 0)
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 2)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 2)
        self.assertEqual(count_Fac(6), 3)
        self.assertEqual(count_Fac(7), 2)
        self.assertEqual(count_Fac(8), 3)
        self.assertEqual(count_Fac(9), 3)
        self.assertEqual(count_Fac(10), 2)

    def test_complex(self):
        self.assertEqual(count_Fac(11), 2)
        self.assertEqual(count_Fac(12), 3)
        self.assertEqual(count_Fac(13), 2)
        self.assertEqual(count_Fac(14), 3)
        self.assertEqual(count_Fac(15), 3)
        self.assertEqual(count_Fac(16), 4)
        self.assertEqual(count_Fac(17), 3)
        self.assertEqual(count_Fac(18), 4)
        self.assertEqual(count_Fac(19), 3)
        self.assertEqual(count_Fac(20), 4)
