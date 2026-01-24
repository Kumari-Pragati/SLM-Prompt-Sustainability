import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):

    def test_valid_dog_ages(self):
        self.assertEqual(dog_age(0), 0)
        self.assertEqual(dog_age(1), 10.5)
        self.assertEqual(dog_age(2), 21)
        self.assertEqual(dog_age(3), 25)
        self.assertEqual(dog_age(10), 59)

    def test_edge_cases(self):
        self.assertEqual(dog_age(-1), None)
        self.assertEqual(dog_age(0.5), 5.25)
        self.assertEqual(dog_age(2.5), 21)

    def test_invalid_input(self):
        with self.assertRaises(SystemExit):
            dog_age(-10)

    def test_typical_dog_ages(self):
        self.assertAlmostEqual(dog_age(1.5), 15.75)
        self.assertAlmostEqual(dog_age(2.9), 21 + (2.9 - 2) * 4)
