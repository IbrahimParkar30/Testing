import unittest

class StudentGrades:
    def __init__(self):
        self.grades = {}

    def add_grade(self, student_name, grade):
        """Adds a grade for the specified student."""
        if student_name in self.grades:
            self.grades[student_name].append(grade)
        else:
            self.grades[student_name] = [grade]

    def get_grades(self, student_name):
        """Retrieves the list of grades for the specified student."""
        return self.grades.get(student_name, [])

    def get_average_grade(self, student_name):
        """Calculates and returns the average grade for the specified student."""
        grades = self.get_grades(student_name)
        if grades:
            return sum(grades) / len(grades)
        return None


class TestStudentGrades(unittest.TestCase):
    def setUp(self):
        """Initialize a StudentGrades instance and add sample data."""
        self.student_grades = StudentGrades()
        self.student_grades.add_grade('Alice', 85)
        self.student_grades.add_grade('Alice', 90)
        self.student_grades.add_grade('Bob', 75)

    def test_add_grade_new_student(self):
        """Test adding a grade for a new student."""
        self.student_grades.add_grade('Charlie', 80)
        self.assertEqual(self.student_grades.get_grades('Charlie'), [80])

    def test_add_grade_existing_student(self):
        """Test adding an additional grade for an existing student."""
        self.student_grades.add_grade('Alice', 95)
        self.assertEqual(self.student_grades.get_grades('Alice'), [85, 90, 95])

    def test_get_grades_existing_student(self):
        """Test retrieving grades for an existing student."""
        self.assertEqual(self.student_grades.get_grades('Alice'), [85, 90])

    def test_get_grades_nonexistent_student(self):
        """Test retrieving grades for a student not in the system."""
        self.assertEqual(self.student_grades.get_grades('Diana'), [])

    def test_get_average_grade(self):
        """Test calculating the average grade for a student."""
        self.assertAlmostEqual(self.student_grades.get_average_grade('Alice'), 87.5)

    def test_get_average_grade_no_grades(self):
        """Test calculating the average grade for a student with no grades."""
        self.assertIsNone(self.student_grades.get_average_grade('Diana'))

if __name__ == '__main__':
    unittest.main()
