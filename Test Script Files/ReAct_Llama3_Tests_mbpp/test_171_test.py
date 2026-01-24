import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):

    def test_perimeter_pentagon_typical(self):
        self.assertEqual(perimeter_pentagon(5), 25)

    def test_perimeter_pentagon_edge(self):
        self.assertEqual(perimeter_pentagon(0), 0)

    def test_perimeter_pentagon_edge2(self):
        self.assertEqual(perimeter_pentagon(10), 50)

    def test_perimeter_pentagon_edge3(self):
        self.assertEqual(perimeter_pentagon(-5), 0)

    def test_perimeter_pentagon_edge4(self):
        self.assertEqual(perimeter_pentagon(5.5), 27.5)

    def test_perimeter_pentagon_edge5(self):
        self.assertEqual(perimeter_pentagon(-10), 0)
