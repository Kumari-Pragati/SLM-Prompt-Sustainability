import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):
    def test_positive_numbers(self):
        expected_result = [
            [['*' for _ in range(3)] for _ in range(3)] for _ in range(3)
        ]
        self.assertEqual(array_3d(3, 3, 3), expected_result)

    def test_zero(self):
        expected_result = [
            [['*' for _ in range(0)] for _ in range(3)] for _ in range(3)
        ]
        self.assertEqual(array_3d(0, 3, 3), expected_result)

    def test_negative_numbers(self):
        expected_result = [
            [['*' for _ in range(-3)] for _ in range(3)] for _ in range(3)
        ]
        self.assertEqual(array_3d(-3, 3, 3), expected_result)

    def test_one_dimension(self):
        expected_result = [
            ['*']
        ]
        self.assertEqual(array_3d(1, 1, 1), expected_result)

    def test_two_dimensions(self):
        expected_result = [
            [['*'] for _ in range(3)]
        ]
        self.assertEqual(array_3d(1, 3, 1), expected_result)

    def test_zero_dimensions(self):
        self.assertEqual(array_3d(0, 0, 0), [])
