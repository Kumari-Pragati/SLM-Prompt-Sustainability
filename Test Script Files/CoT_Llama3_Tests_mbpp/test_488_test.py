import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):

    def test_area_pentagon_typical(self):
        self.assertAlmostEqual(area_pentagon(5), 12.5, places=1)

    def test_area_pentagon_edge(self):
        self.assertAlmostEqual(area_pentagon(0), 0, places=1)

    def test_area_pentagon_edge2(self):
        self.assertAlmostEqual(area_pentagon(1), 0.7853981633974483, places=5)

    def test_area_pentagon_invalid_input(self):
        with self.assertRaises(TypeError):
            area_pentagon('a')

    def test_area_pentagon_invalid_input2(self):
        with self.assertRaises(TypeError):
            area_pentagon(None)

    def test_area_pentagon_invalid_input3(self):
        with self.assertRaises(TypeError):
            area_pentagon(5.5, 6)

    def test_area_pentagon_invalid_input4(self):
        with self.assertRaises(TypeError):
            area_pentagon([5, 6])
