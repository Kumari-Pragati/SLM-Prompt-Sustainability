import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):

    def test_valid_dog_ages(self):
        self.assertEqual(dog_age(0), 0)
        self.assertAlmostEqual(dog_age(1), 10.5, places=1)
        self.assertAlmostEqual(dog_age(2), 21, places=1)
        self.assertAlmostEqual(dog_age(3), 25, places=1)
        self.assertAlmostEqual(dog_age(4), 29, places=1)

    def test_invalid_dog_age(self):
        with self.assertRaises(SystemExit):
            dog_age(-1)

    def test_edge_cases(self):
        self.assertAlmostEqual(dog_age(2.5), 21.5, places=1)
        self.assertAlmostEqual(dog_age(2.999), 21, places=1)
