import unittest
from mbpp_535_code import topbottom_surfacearea

class TestTopbottomSurfacearea(unittest.TestCase):
    def test_simple_inputs(self):
        self.assertEqual(topbottom_surfacearea(1), 3.1415)
        self.assertEqual(topbottom_surfacearea(2), 12.5664)
        self.assertEqual(topbottom_surfacearea(3), 31.4159)

    def test_edge_cases(self):
        self.assertEqual(topbottom_surfacearea(0), 0)
        self.assertEqual(topbottom_surfacearea(-1), 3.1415)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            topbottom_surfacearea("a")
        with self.assertRaises(TypeError):
            topbottom_surfacearea(None)
