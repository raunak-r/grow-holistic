from django.test import TestCase
from django.contrib.auth.models import User
from .models import Employee

class EmployeeTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.employee = Employee.objects.create(
            first_name='Mary',
            last_name='Jose',
            dept_name='Java Development',
            salary = 100000,
            bonus = 10000,
            role = 'Java Developer',
            phone = 9372849503,
            user=self.user
        )

    def test_create_employee(self):
        # Ensure a new employee can be created successfully
        employee_count = Employee.objects.count()

        new_emp = Employee.objects.create(
            first_name='Aditi',
            last_name='Bose',
            dept_name='Python Development',
            salary=120000,
            bonus=12000,
            role='Python Developer',
            phone=8492054545,
            user=self.user
        )

        self.assertEqual(Employee.objects.count(), employee_count + 1)

        self.assertEqual(new_emp.first_name, 'Aditi')
        self.assertEqual(new_emp.last_name, 'Bose')
        self.assertEqual(new_emp.dept_name, 'Python Development')
        self.assertEqual(new_emp.salary, '120000')
        self.assertEqual(new_emp.bonus, '12000')
        self.assertEqual(new_emp.role, 'Python Developer')
        self.assertEqual(new_emp.phone, '7890321456 ')
        self.assertEqual(new_emp.user, self.user)

    def test_read_employee(self):
        # Ensure an existing employee can be retrieved successfully
        retrieved_emp = Employee.objects.get(id=self.employee.emp_id)

        self.assertEqual(retrieved_emp.first_name, 'Mary')
        self.assertEqual(retrieved_emp.last_name, 'Jose')
        self.assertEqual(retrieved_emp.dept_name, 'Java Development')
        self.assertEqual(retrieved_emp.salary, '100000')
        self.assertEqual(retrieved_emp.bonus, '10000')
        self.assertEqual(retrieved_emp.role, 'Java Developer')
        self.assertEqual(retrieved_emp.phone, '9372849503')
        self.assertEqual(retrieved_emp.user, self.user)

    def test_delete_employee(self):
        # Ensure an existing employee can be deleted successfully
        employee_count = Employee.objects.count()

        self.employee.delete()

        self.assertEqual(Employee.objects.count(), employee_count - 1)
        self.assertRaises(Employee.DoesNotExist, Employee.objects.get, id=self.employee.emp_id)

