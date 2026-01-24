import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(dog_age(0), 0)
        self.assertAlmostEqual(dog_age(1), 10.5, places=1)
        self.assertAlmostEqual(dog_age(2), 21, places=1)
        self.assertAlmostEqual(dog_age(3), 25, places=1)
        self.assertAlmostEqual(dog_age(4), 29, places=1)

    def test_edge_cases(self):
        self.assertEqual(dog_age(-1), None)  # invalid input
        self.assertEqual(dog_age(2), 21)
        self.assertEqual(dog_age(100), 124)

    def test_boundary_cases(self):
        self.assertAlmostEqual(dog_age(2.5), 21.5, places=1)
        self.assertAlmostEqual(dog_age(2.9), 21.9, places=1)

    def test_corner_cases(self):
        self.assertEqual(dog_age(0.5), 5.25)
        self.assertEqual(dog_age(1.5), 15.75)
