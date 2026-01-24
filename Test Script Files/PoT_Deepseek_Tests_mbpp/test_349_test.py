import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(check('0101'), 'Yes')
        self.assertEqual(check('1010'), 'Yes')
        self.assertEqual(check('0000'), 'Yes')
        self.assertEqual(check('1111'), 'Yes')

    def test_edge_cases(self):
        self.assertEqual(check(''), 'Yes')
        self.assertEqual(check('0'), 'Yes')
        self.assertEqual(check('1'), 'Yes')

    def test_boundary_cases(self):
        self.assertEqual(check('0' * 1000), 'Yes')
        self.assertEqual(check('1' * 1000), 'Yes')

    def test_invalid_inputs(self):
        self.assertEqual(check('1020'), 'No')
        self.assertEqual(check('2010'), 'No')
        self.assertEqual(check('0120'), 'No')
        self.assertEqual(check('0102'), 'No')
        self.assertEqual(check('1122'), 'No')
        self.assertEqual(check('1212'), 'No')
        self.assertEqual(check('2222'), 'No')
