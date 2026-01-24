import unittest
from mbpp_764_code import number_ctr

class TestNumberCtr(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(number_ctr('12345'), 5)
        self.assertEqual(number_ctr('123'), 3)
        self.assertEqual(number_ctr('1'), 1)
        self.assertEqual(number_ctr(''), 0)
        self.assertEqual(number_ctr('012345'), 5)
        self.assertEqual(number_ctr('987654321'), 10)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(number_ctr('0'), 1)
        self.assertEqual(number_ctr('9'), 1)
        self.assertEqual(number_ctr('10'), 1)
        self.assertEqual(number_ctr('999999999'), 10)
        self.assertEqual(number_ctr('-12345'), 0)
        self.assertEqual(number_ctr('12345a'), 5)
        self.assertEqual(number_ctr('12345X'), 5)
        self.assertEqual(number_ctr('12345_'), 5)
