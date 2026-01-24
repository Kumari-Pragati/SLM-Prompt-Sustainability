import unittest
from mbpp_321_code import find_demlo

class TestFindDemlo(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_demlo('abc'), '12321')
        self.assertEqual(find_demlo('123'), '12321')
        self.assertEqual(find_demlo('xyz'), '12321')

    def test_edge_cases(self):
        self.assertEqual(find_demlo(''), '')
        self.assertEqual(find_demlo('a'), '1')
        self.assertEqual(find_demlo('1'), '1')

    def test_boundary_cases(self):
        self.assertEqual(find_demlo('1234567890'), '1234567890987654321')
        self.assertEqual(find_demlo('0'), '10')
