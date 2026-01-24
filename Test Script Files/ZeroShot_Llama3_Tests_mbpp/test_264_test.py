import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):

    def test_dog_age_valid(self):
        self.assertAlmostEqual(dog_age(0), 0, places=1)
        self.assertAlmostEqual(dog_age(1), 10.5, places=1)
        self.assertAlmostEqual(dog_age(2), 21, places=1)
        self.assertAlmostEqual(dog_age(3), 25, places=1)
        self.assertAlmostEqual(dog_age(4), 29, places=1)
        self.assertAlmostEqual(dog_age(5), 33, places=1)

    def test_dog_age_invalid(self):
        with self.assertRaises(SystemExit):
            dog_age(-1)
