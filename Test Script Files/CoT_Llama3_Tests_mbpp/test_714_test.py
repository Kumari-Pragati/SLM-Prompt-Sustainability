import unittest
from mbpp_714_code import count_Fac

class TestCountFac(unittest.TestCase):

    def test_count_Fac_typical(self):
        self.assertEqual(count_Fac(10), 2)
        self.assertEqual(count_Fac(12), 3)
        self.assertEqual(count_Fac(15), 3)

    def test_count_Fac_edge(self):
        self.assertEqual(count_Fac(1), 0)
        self.assertEqual(count_Fac(2), 1)
        self.assertEqual(count_Fac(3), 1)

    def test_count_Fac_boundary(self):
        self.assertEqual(count_Fac(4), 1)
        self.assertEqual(count_Fac(5), 1)
        self.assertEqual(count_Fac(6), 2)

    def test_count_Fac_invalid(self):
        with self.assertRaises(TypeError):
            count_Fac('a')
        with self.assertRaises(TypeError):
            count_Fac(None)
