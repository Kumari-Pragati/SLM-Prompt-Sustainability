import unittest
from mbpp_731_code import lateralsurface_cone

class TestLateralsurfaceCone(unittest.TestCase):

    def test_lateralsurface_cone(self):
        self.assertAlmostEqual(lateralsurface_cone(1,1), math.pi * 1 * math.sqrt(1**2 + 1**2), places=5)
        self.assertAlmostEqual(lateralsurface_cone(2,2), math.pi * 2 * math.sqrt(2**2 + 2**2), places=5)
        self.assertAlmostEqual(lateralsurface_cone(3,3), math.pi * 3 * math.sqrt(3**2 + 3**2), places=5)
        self.assertAlmostEqual(lateralsurface_cone(4,4), math.pi * 4 * math.sqrt(4**2 + 4**2), places=5)
        self.assertAlmostEqual(lateralsurface_cone(5,5), math.pi * 5 * math.sqrt(5**2 + 5**2), places=5)
