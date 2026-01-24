import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(match('ABCdef'), 'Yes')
        self.assertEqual(match('ABCdeF'), 'Yes')
        self.assertEqual(match('ABCdEf'), 'Yes')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(match('ABC'), 'No')
        self.assertEqual(match('ABCdef '), 'No')
        self.assertEqual(match('ABCdef1'), 'No')
        self.assertEqual(match('123ABCdef'), 'No')
        self.assertEqual(match('ABCdefG'), 'No')
        self.assertEqual(match('ABCdef_'), 'No')
        self.assertEqual(match('ABCdef0'), 'No')

    def test_special_inputs(self):
        self.assertEqual(match('ABCdef!'), 'No')
        self.assertEqual(match('ABCdef@'), 'No')
        self.assertEqual(match('ABCdef#'), 'No')
        self.assertEqual(match('ABCdef$'), 'No')
        self.assertEqual(match('ABCdef%'), 'No')
        self.assertEqual(match('ABCdef&'), 'No')
        self.assertEqual(match('ABCdef*'), 'No')
        self.assertEqual(match('ABCdef?'), 'No')
        self.assertEqual(match('ABCdef('), 'No')
        self.assertEqual(match('ABCdef)'), 'No')
        self.assertEqual(match('ABCdef['), 'No')
        self.assertEqual(match('ABCdef]'), 'No')
        self.assertEqual(match('ABCdef{'), 'No')
        self.assertEqual(match('ABCdef}'), 'No')
        self.assertEqual(match('ABCdef|'), 'No')
