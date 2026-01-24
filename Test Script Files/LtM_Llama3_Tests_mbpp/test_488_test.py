import unittest
from mbpp_488_code import area_pentagon

class TestAreaPentagon(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertAlmostEqual(area_pentagon(1), 0.5396)
        self.assertAlmostEqual(area_pentagon(2), 2.1764)
        self.assertAlmostEqual(area_pentagon(3), 4.8132)

    def test_edge_cases(self):
        self.assertAlmostEqual(area_pentagon(0), 0)
        self.assertAlmostEqual(area_pentagon(10), 11.3184)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            area_pentagon('a')
        with self.assertRaises(TypeError):
            area_pentagon(None)
