import unittest
from mbpp_264_code import dog_age

class TestDogAge(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(dog_age(1), 10.5)
        self.assertEqual(dog_age(2), 21)
        self.assertEqual(dog_age(3), 25)

    def test_boundary_conditions(self):
        self.assertEqual(dog_age(0), 0)
        self.assertEqual(dog_age(2), 21)

    def test_invalid_input(self):
        with self.assertRaises(SystemExit):
            dog_age(-1)
