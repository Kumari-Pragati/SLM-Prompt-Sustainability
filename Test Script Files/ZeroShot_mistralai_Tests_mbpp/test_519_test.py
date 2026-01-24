import unittest
from mbpp_519_code import sqrt, pi
from 519_code import volume_tetrahedron

class TestVolumeTetrahedron(unittest.TestCase):

    def test_volume_tetrahedron_with_positive_numbers(self):
        test_cases = [(1, 0.43301270189221994),
                       (2, 5.196152422735335),
                       (3, 20.64656304923993)]

        for num, expected_volume in test_cases:
            with self.subTest(num=num):
                result = volume_tetrahedron(num)
                self.assertAlmostEqual(result, expected_volume, delta=0.01)

    def test_volume_tetrahedron_with_zero(self):
        with self.assertRaises(ValueError):
            volume_tetrahedron(0)

    def test_volume_tetrahedron_with_negative_numbers(self):
        test_cases = [(-1, -0.43301270189221994),
                       (-2, -5.196152422735335)]

        for num, expected_volume in test_cases:
            with self.subTest(num=num):
                result = volume_tetrahedron(num)
                self.assertAlmostEqual(result, expected_volume, delta=0.01)
