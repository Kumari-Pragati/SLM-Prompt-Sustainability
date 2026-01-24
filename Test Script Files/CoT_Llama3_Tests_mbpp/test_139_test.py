import unittest
from mbpp_139_code import circle_cumference

class TestCircleCircumference(unittest.TestCase):
    def test_typical_input(self):
        self.assertAlmostEqual(circle_circumference(5), 31.4159, places=5)

    def test_edge_case_zero(self):
        self.assertAlmostEqual(circle_circumference(0), 0, places=5)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            circle_circumference(-5)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            circle_circumference('five')

    def test_edge_case_non_numeric2(self):
        with self.assertRaises(TypeError):
            circle_circumference([5, 5])

    def test_edge_case_non_numeric3(self):
        with self.assertRaises(TypeError):
            circle_circumference({'five': 5})

    def test_edge_case_non_numeric4(self):
        with self.assertRaises(TypeError):
            circle_circumference(None)
