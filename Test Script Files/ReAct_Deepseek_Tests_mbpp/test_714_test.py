import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 2)
        self.assertEqual(count_Fac(4), 2)
        self.assertEqual(count_Fac(5), 2)
        self.assertEqual(count_Fac(6), 3)
        self.assertEqual(count_Fac(7), 3)
        self.assertEqual(count_Fac(8), 3)
        self.assertEqual(count_Fac(9), 3)
        self.assertEqual(count_Fac(10), 4)

    def test_edge_cases(self):
        self.assertEqual(count_Fac(0), 0)
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(100), 24)
        self.assertEqual(count_Fac(1000), 21)
        self.assertEqual(count_Fac(10000), 20)

    def test_explicitly_handled_error_cases(self):
        with self.assertRaises(TypeError):
            count_Fac('a')
        with self.assertRaises(TypeError):
            count_Fac(None)
        with self.assertRaises(TypeError):
            count_Fac([])
        with self.assertRaises(TypeError):
            count_Fac({})
