from django.core.management.base import BaseCommand
from students.models import Student, Parent
from datetime import date

class Command(BaseCommand):
    help = 'Add demo student records to the database.'

    def handle(self, *args, **options):
        demo_data = [
            # Existing demo students
            # ...existing code...
            # Additional demo students
            {
                'first_name': 'Kiran', 'last_name': 'Varma', 'student_id': '2026009', 'gender': 'Male',
                'date_of_birth': date(2010, 4, 10), 'class_name': '10A',
                'parent': {'father_name': 'Mohan Varma', 'mother_name': 'Deepa Varma', 'phone': '9876543218'}
            },
            {
                'first_name': 'Priya', 'last_name': 'Suresh', 'student_id': '2026010', 'gender': 'Female',
                'date_of_birth': date(2010, 6, 15), 'class_name': '10B',
                'parent': {'father_name': 'Suresh Kumar', 'mother_name': 'Lalitha Suresh', 'phone': '9876543219'}
            },
            {
                'first_name': 'Manoj', 'last_name': 'Patel', 'student_id': '2026011', 'gender': 'Male',
                'date_of_birth': date(2010, 1, 22), 'class_name': '10A',
                'parent': {'father_name': 'Ramesh Patel', 'mother_name': 'Meena Patel', 'phone': '9876543220'}
            },
            {
                'first_name': 'Neha', 'last_name': 'Joshi', 'student_id': '2026012', 'gender': 'Female',
                'date_of_birth': date(2010, 10, 30), 'class_name': '10B',
                'parent': {'father_name': 'Sanjay Joshi', 'mother_name': 'Kavita Joshi', 'phone': '9876543221'}
            },
        ]
            {
                'first_name': 'Arjun', 'last_name': 'Nair', 'student_id': '2026001', 'gender': 'Male',
                'date_of_birth': date(2010, 5, 12), 'class_name': '10A',
                'parent': {'father_name': 'Suresh Nair', 'mother_name': 'Lakshmi Nair', 'phone': '9876543210'}
            },
            {
                'first_name': 'Meera', 'last_name': 'Thomas', 'student_id': '2026002', 'gender': 'Female',
                'date_of_birth': date(2010, 8, 23), 'class_name': '10B',
                'parent': {'father_name': 'Thomas Mathew', 'mother_name': 'Anita Mathew', 'phone': '9876543211'}
            },
            {
                'first_name': 'Rahul', 'last_name': 'Menon', 'student_id': '2026003', 'gender': 'Male',
                'date_of_birth': date(2010, 2, 17), 'class_name': '10A',
                'parent': {'father_name': 'Geetha Menon', 'mother_name': 'Ramesh Menon', 'phone': '9876543212'}
            },
            {
                'first_name': 'Anjali', 'last_name': 'Pillai', 'student_id': '2026004', 'gender': 'Female',
                'date_of_birth': date(2010, 11, 5), 'class_name': '10B',
                'parent': {'father_name': 'Ravi Pillai', 'mother_name': 'Sunitha Pillai', 'phone': '9876543213'}
            },
            {
                'first_name': 'Vishnu', 'last_name': 'Das', 'student_id': '2026005', 'gender': 'Male',
                'date_of_birth': date(2010, 3, 14), 'class_name': '10A',
                'parent': {'father_name': 'Prakash Das', 'mother_name': 'Latha Das', 'phone': '9876543214'}
            },
            {
                'first_name': 'Sneha', 'last_name': 'Ramesh', 'student_id': '2026006', 'gender': 'Female',
                'date_of_birth': date(2010, 7, 19), 'class_name': '10B',
                'parent': {'father_name': 'Ramesh Kumar', 'mother_name': 'Shobha Ramesh', 'phone': '9876543215'}
            },
            {
                'first_name': 'Amit', 'last_name': 'Sharma', 'student_id': '2026007', 'gender': 'Male',
                'date_of_birth': date(2010, 9, 25), 'class_name': '10A',
                'parent': {'father_name': 'Rajesh Sharma', 'mother_name': 'Kavita Sharma', 'phone': '9876543216'}
            },
            {
                'first_name': 'Divya', 'last_name': 'Krishnan', 'student_id': '2026008', 'gender': 'Female',
                'date_of_birth': date(2010, 12, 2), 'class_name': '10B',
                'parent': {'father_name': 'Krishnan Nair', 'mother_name': 'Maya Krishnan', 'phone': '9876543217'}
            },
        ]

        for data in demo_data:
            parent_obj, _ = Parent.objects.get_or_create(
                father_name=data['parent']['father_name'],
                mother_name=data['parent']['mother_name'],
                phone=data['parent']['phone']
            )
            slug_value = f"{data['first_name'].lower()}-{data['last_name'].lower()}-{data['student_id']}"
            student_obj, created = Student.objects.get_or_create(
                student_id=data['student_id'],
                defaults={
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'gender': data['gender'],
                    'date_of_birth': data['date_of_birth'],
                    'class_name': data['class_name'],
                    'parent': parent_obj,
                    'slug': slug_value
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added student: {student_obj}"))
            else:
                self.stdout.write(self.style.WARNING(f"Student already exists: {student_obj}"))
