import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):
    def test_valid_age(self):
        self.assertEqual(dog_age(0), 0)
        self.assertEqual(dog_age(1), 10.5)
        self.assertEqual(dog_age(2), 21)
        self.assertEqual(dog_age(3), 25.5)
        self.assertEqual(dog_age(10), 121)
        self.assertEqual(dog_age(20), 241)

    def test_negative_age(self):
        with self.assertRaises(SystemExit):
            dog_age(-1)

    def test_zero_or_less_than_zero_age(self):
        with self.assertRaises(SystemExit):
            dog_age(0)
            dog_age(-1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            dog_age('string')
