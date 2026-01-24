import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):
    def test_typical_use_case(self):
        m = 2
        n = 3
        o = 4
        result = array_3d(m, n, o)
        self.assertEqual(len(result), o)
        for row in result:
            self.assertEqual(len(row), n)
            for col in row:
                self.assertEqual(len(col), m)
                for i in col:
                    self.assertEqual(i, '*')

    def test_edge_case_m_zero(self):
        m = 0
        n = 3
        o = 4
        with self.assertRaises(ValueError):
            array_3d(m, n, o)

    def test_edge_case_n_zero(self):
        m = 2
        n = 0
        o = 4
        with self.assertRaises(ValueError):
            array_3d(m, n, o)

    def test_edge_case_o_zero(self):
        m = 2
        n = 3
        o = 0
        with self.assertRaises(ValueError):
            array_3d(m, n, o)

    def test_edge_case_m_negative(self):
        m = -1
        n = 3
        o = 4
        with self.assertRaises(ValueError):
            array_3d(m, n, o)

    def test_edge_case_n_negative(self):
        m = 2
        n = -1
        o = 4
        with self.assertRaises(ValueError):
            array_3d(m, n, o)

    def test_edge_case_o_negative(self):
        m = 2
        n = 3
        o = -1
        with self.assertRaises(ValueError):
            array_3d(m, n, o)
