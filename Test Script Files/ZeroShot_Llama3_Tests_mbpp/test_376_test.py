import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):

    def test_remove_replica(self):
        self.assertEqual(remove_replica((1, 2, 3)), (1, 2, 3))
        self.assertEqual(remove_replica((1, 1, 2, 2, 3, 3)), (1, 2, 3))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica(('MSP', 'MSP', 'MSP')), ('MSP', 'MSP', 'MSP'))
        self.assertEqual(remove_replica((1, 2, 3, 'MSP', 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 'MSP')), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 'MSP', 4, 5, 1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 'MSP', 1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 'MSP', 4, 5, 1, 2, 3, 4, 5, 'MSP')), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 'MSP', 1, 2, 3, 4, 5, 'MSP')), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'MSP')), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 'MSP', 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 'MSP', 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'MSP', 1, 2, 3, 4, 5)), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 'MSP', 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'MSP')), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 'MSP', 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 'MSP')), (1, 2, 3, 4, 5))
        self.assertEqual(remove_replica((1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4,