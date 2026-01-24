import unittest
from mbpp_171_code import perimeter_pentagon

class TestPerimeterPentagon(unittest.TestCase):

    def test_perimeter_pentagon(self):
        self.assertEqual(perimeter_pentagon(5), 25)
        self.assertEqual(perimeter_pentagon(10), 50)
        self.assertEqual(perimeter_pentagon(0), 0)
        self.assertNotEqual(perimeter_pentagon(5), 30)
