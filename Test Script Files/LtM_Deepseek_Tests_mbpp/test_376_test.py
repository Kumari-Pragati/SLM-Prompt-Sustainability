import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(remove_replica(('a', 'b', 'c')), ('a', 'b', 'c'))
        self.assertEqual(remove_replica((1, 2, 3)), (1, 2, 3))
        self.assertEqual(remove_replica(('1', '2', '3')), ('1', '2', '3'))

    def test_edge_conditions(self):
        self.assertEqual(remove_replica(()), ())
        self.assertEqual(remove_replica(('a',)), ('a',))
        self.assertEqual(remove_replica(('a', 'a')), ('a', 'MSP'))

    def test_complex_cases(self):
        self.assertEqual(remove_replica(('a', 'a', 'b', 'b')), ('a', 'MSP', 'b', 'MSP'))
        self.assertEqual(remove_replica(('a', 'b', 'a', 'b')), ('a', 'b', 'MSP', 'MSP'))
        self.assertEqual(remove_replica(('a', 'a', 'a', 'a')), ('a', 'MSP', 'MSP', 'MSP'))
