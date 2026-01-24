import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):

    def test_negative_age(self):
        self.assertRaises(SystemExit, dog_age, -1)

    def test_zero_age(self):
        self.assertEqual(dog_age(0), 0)

    def test_first_two_years(self):
        self.assertEqual(dog_age(1), 10.5)
        self.assertEqual(dog_age(2), 21)

    def test_more_than_two_years(self):
        self.assertEqual(dog_age(3), 25.5)
        self.assertEqual(dog_age(5), 33)
