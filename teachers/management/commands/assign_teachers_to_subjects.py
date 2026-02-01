from django.core.management.base import BaseCommand
from teachers.models import Teacher
from subjects.models import Subject

class Command(BaseCommand):
    help = 'Assign teachers to subjects for demo purposes.'

    def handle(self, *args, **options):
        assignments = [
            # (teacher_email, [subject_codes])
            ('ravi.menon@school.com', ['MATH101', 'MATH102']),
            ('anita.krishnan@school.com', ['SCI101', 'SCI102']),
            ('suresh.patel@school.com', ['ENG101', 'ENG102']),
            ('meena.sharma@school.com', ['SOC101', 'SOC102']),
            ('ajay.kumar@school.com', ['CS101', 'CS102']),
            ('priya.nair@school.com', ['MATH101']),
            ('vikram.joshi@school.com', ['SCI101']),
            ('divya.rao@school.com', ['ENG101']),
            ('sunil.pillai@school.com', ['SOC101']),
            ('kavita.das@school.com', ['CS101']),
        ]
        for email, subject_codes in assignments:
            try:
                teacher = Teacher.objects.get(email=email)
                subjects = Subject.objects.filter(code__in=subject_codes)
                teacher.subjects.set(subjects)
                self.stdout.write(self.style.SUCCESS(f"Assigned {teacher} to subjects: {[s.name for s in subjects]}"))
            except Teacher.DoesNotExist:
                self.stdout.write(self.style.WARNING(f"Teacher not found: {email}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(str(e)))
