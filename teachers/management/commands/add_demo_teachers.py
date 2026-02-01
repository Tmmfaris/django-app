from django.core.management.base import BaseCommand
from teachers.models import Teacher

class Command(BaseCommand):
    help = 'Add demo teacher records to the database.'

    def handle(self, *args, **options):
        demo_teachers = [
            {'first_name': 'Ravi', 'last_name': 'Menon', 'email': 'ravi.menon@school.com', 'phone': '987650001', 'department': 'Mathematics'},
            {'first_name': 'Anita', 'last_name': 'Krishnan', 'email': 'anita.krishnan@school.com', 'phone': '987650002', 'department': 'Science'},
            {'first_name': 'Suresh', 'last_name': 'Patel', 'email': 'suresh.patel@school.com', 'phone': '987650003', 'department': 'English'},
            {'first_name': 'Meena', 'last_name': 'Sharma', 'email': 'meena.sharma@school.com', 'phone': '987650004', 'department': 'Social Studies'},
            {'first_name': 'Ajay', 'last_name': 'Kumar', 'email': 'ajay.kumar@school.com', 'phone': '987650005', 'department': 'Computer Science'},
            {'first_name': 'Priya', 'last_name': 'Nair', 'email': 'priya.nair@school.com', 'phone': '987650006', 'department': 'Mathematics'},
            {'first_name': 'Vikram', 'last_name': 'Joshi', 'email': 'vikram.joshi@school.com', 'phone': '987650007', 'department': 'Science'},
            {'first_name': 'Divya', 'last_name': 'Rao', 'email': 'divya.rao@school.com', 'phone': '987650008', 'department': 'English'},
            {'first_name': 'Sunil', 'last_name': 'Pillai', 'email': 'sunil.pillai@school.com', 'phone': '987650009', 'department': 'Social Studies'},
            {'first_name': 'Kavita', 'last_name': 'Das', 'email': 'kavita.das@school.com', 'phone': '987650010', 'department': 'Computer Science'},
        ]
        for data in demo_teachers:
            obj, created = Teacher.objects.get_or_create(
                email=data['email'],
                defaults={
                    'first_name': data['first_name'],
                    'last_name': data['last_name'],
                    'phone': data['phone'],
                    'department': data['department']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added teacher: {obj}"))
            else:
                self.stdout.write(self.style.WARNING(f"Teacher already exists: {obj}"))
