import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):
    def test_perimeter_typical(self):
        self.assertEqual(perimeter_pentagon(5), 25)
        self.assertEqual(perimeter_pentagon(10), 50)

    def test_perimeter_edge(self):
        self.assertEqual(perimeter_pentagon(0), 0)
        self.assertEqual(perimeter_pentagon(1), 5)
        self.assertEqual(perimeter_pentagon(2), 10)

    def test_perimeter_negative(self):
        self.assertRaises(ValueError, perimeter_pentagon, -1)
        self.assertRaises(ValueError, perimeter_pentagon, -5)
