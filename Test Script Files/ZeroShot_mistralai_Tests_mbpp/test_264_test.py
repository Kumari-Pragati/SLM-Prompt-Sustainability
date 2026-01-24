import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):

    def test_negative_age(self):
        with self.assertRaises(SystemExit):
            dog_age(-1)

    def test_age_less_than_or_equal_to_2(self):
        self.assertAlmostEqual(dog_age(0), 0)
        self.assertAlmostEqual(dog_age(1), 10.5)
        self.assertAlmostEqual(dog_age(2), 21)

    def test_age_greater_than_2(self):
        self.assertAlmostEqual(dog_age(3), 25.5)
        self.assertAlmostEqual(dog_age(10), 63)
        self.assertAlmostEqual(dog_age(20), 101)
