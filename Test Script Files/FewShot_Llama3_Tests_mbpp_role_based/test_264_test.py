import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):
    def test_valid_dog_age(self):
        self.assertAlmostEqual(dog_age(1), 10.5)
        self.assertAlmostEqual(dog_age(2), 21)
        self.assertAlmostEqual(dog_age(3), 25)
        self.assertAlmostEqual(dog_age(4), 29)
        self.assertAlmostEqual(dog_age(5), 33)

    def test_zero_dog_age(self):
        self.assertEqual(dog_age(0), 0)

    def test_negative_dog_age(self):
        with self.assertRaises(SystemExit):
            dog_age(-1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            dog_age('a')
