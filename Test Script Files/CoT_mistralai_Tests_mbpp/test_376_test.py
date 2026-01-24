import unittest
from mbpp_376_code import remove_replica

class TestRemoveReplica(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(remove_replica(()), ('MSP',))

    def test_single_element(self):
        self.assertEqual(remove_replica((1,)), (1,))

    def test_duplicate_elements(self):
        self.assertEqual(remove_replica((1, 1, 2, 3)), (1, 2, 3))

    def test_multiple_duplicates(self):
        self.assertEqual(remove_replica((1, 1, 2, 2, 3)), (1, 3))

    def test_no_duplicates(self):
        self.assertEqual(remove_replica((1, 2, 3)), (1, 2, 3))

    def test_replica_in_beginning(self):
        self.assertEqual(remove_replica((1, 1, 2)), (2,))

    def test_replica_in_end(self):
        self.assertEqual(remove_replica((1, 2, 1)), (1, 2))

    def test_replica_in_middle(self):
        self.assertEqual(remove_replica((1, 1, 2, 3)), (1, 2, 3))

    def test_replica_at_boundary(self):
        self.assertEqual(remove_replica((1, 1, 2, 3, 1)), (1, 2, 3))

    def test_invalid_input_empty_set(self):
        with self.assertRaises(TypeError):
            remove_replica({})

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            remove_replica('test')
