import unittest
from mbpp_959_code import Average

class TestAverage(unittest.TestCase):

    def test_average_normal(self):
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(Average([0, 0, 0, 0, 0]), 0.0)
        self.assertAlmostEqual(Average([10, 20, 30, 40, 50]), 30.0)

    def test_average_edge_cases(self):
        self.assertAlmostEqual(Average([1]), 1.0)
        self.assertAlmostEqual(Average([1, 2]), 1.5)
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5, 6]), 3.5)
        self.assertAlmostEqual(Average([1, 2, 3, 4, 5, 6, 7]), 4.0)

    def test_average_empty_list(self):
        self.assertEqual(Average([]), 0.0)

    def test_average_negative_numbers(self):
        self.assertAlmostEqual(Average([-1, -2, -3]), -2.0)
        self.assertAlmostEqual(Average([1, -2, 3]), 1.0)
        self.assertAlmostEqual(Average([-1, 0, -1]), -0.5)

    def test_average_floats(self):
        self.assertAlmostEqual(Average([1.1, 2.2, 3.3]), 2.2)
        self.assertAlmostEqual(Average([0.1, 0.2, 0.3]), 0.2)
