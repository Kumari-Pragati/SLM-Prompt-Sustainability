import unittest
from mbpp_64_code import subject_marks

class TestSubjectMarks(unittest.TestCase):
    def test_typical_use_case(self):
        subjectmarks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
        expected_output = [('Science', 90), ('Maths', 97), ('English', 88), ('Social sciences', 82)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_edge_case(self):
        subjectmarks = [('English', 100)]
        expected_output = [('English', 100)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_boundary_case(self):
        subjectmarks = [('English', 0), ('Science', 50), ('Maths', 100)]
        expected_output = [('Maths', 100), ('Science', 50), ('English', 0)]
        self.assertEqual(subject_marks(subjectmarks), expected_output)

    def test_invalid_input(self):
        subjectmarks = 'invalid input'
        with self.assertRaises(TypeError):
            subject_marks(subjectmarks)
