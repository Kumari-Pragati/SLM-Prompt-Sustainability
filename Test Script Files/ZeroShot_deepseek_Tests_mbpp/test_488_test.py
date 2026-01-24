import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):

    def test_area_pentagon(self):
        self.assertAlmostEqual(area_pentagon(1), 0.589048622547, places=7)
        self.assertAlmostEqual(area_pentagon(2), 2.35619449019, places=7)
        self.assertAlmostEqual(area_pentagon(0), 0)
        self.assertAlmostEqual(area_pentagon(1.5), 1.08308987656)
