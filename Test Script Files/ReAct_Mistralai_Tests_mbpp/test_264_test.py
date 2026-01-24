import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):

    def test_positive_age(self):
        self.assertEqual(dog_age(1), 10.5)
        self.assertEqual(dog_age(2), 21)
        self.assertEqual(dog_age(3), 25.5)

    def test_zero_age(self):
        self.assertEqual(dog_age(0), 0)

    def test_negative_age(self):
        with self.assertRaises(SystemExit):
            dog_age(-1)

    def test_large_age(self):
        self.assertEqual(dog_age(100), 221)

    def test_floating_point_age(self):
        self.assertAlmostEqual(dog_age(2.5), 26.3)
