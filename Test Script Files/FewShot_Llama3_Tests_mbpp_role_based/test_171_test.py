import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):
    def test_perimeter_positive_side_length(self):
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_perimeter_zero_side_length(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_perimeter_negative_side_length(self):
        self.assertEqual(perimeter_pentagon(-5), 25)

    def test_perimeter_non_numeric_side_length(self):
        with self.assertRaises(TypeError):
            perimeter_pentagon("five")
