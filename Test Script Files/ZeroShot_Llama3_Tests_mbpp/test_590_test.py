import unittest
from mbpp_590_code import polar_rect

class TestPolarRect(unittest.TestCase):

    def test_polar_rect(self):
        cn, cn1 = polar_rect(1, 2)
        self.assertEqual(cmath.phase(cn), cmath.pi)
        self.assertEqual(cmath.rect(2, cmath.pi), cn1)

    def test_polar_rect_zero(self):
        cn, cn1 = polar_rect(0, 0)
        self.assertEqual(cmath.phase(cn), 0)
        self.assertEqual(cmath.rect(2, cmath.pi), cn1)

    def test_polar_rect_negative(self):
        cn, cn1 = polar_rect(-1, -2)
        self.assertEqual(cmath.phase(cn), cmath.pi)
        self.assertEqual(cmath.rect(2, cmath.pi), cn1)

    def test_polar_rect_complex(self):
        cn, cn1 = polar_rect(1j, 2j)
        self.assertEqual(cmath.phase(cn), cmath.pi)
        self.assertEqual(cmath.rect(2, cmath.pi), cn1)
