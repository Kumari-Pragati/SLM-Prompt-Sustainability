import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):
    def test_negative_age(self):
        with self.assertRaises(SystemExit):
            dog_age(-1)

    def test_zero_age(self):
        self.assertEqual(dog_age(0), 0)

    def test_one_year(self):
        self.assertAlmostEqual(dog_age(1), 10.5)

    def test_two_years(self):
        self.assertEqual(dog_age(2), 21)

    def test_three_years(self):
        self.assertAlmostEqual(dog_age(3), 25)

    def test_four_years(self):
        self.assertAlmostEqual(dog_age(4), 29)

    def test_five_years(self):
        self.assertAlmostEqual(dog_age(5), 33)

    def test_large_age(self):
        self.assertAlmostEqual(dog_age(10), 69)
