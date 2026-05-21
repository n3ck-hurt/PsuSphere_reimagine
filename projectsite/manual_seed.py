import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectsite.settings')
django.setup()

from studentorg.models import College, Program, Organization, Student, OrgMember
from datetime import date

# Add 8 Colleges
colleges = []
for i in range(1, 9):
    c = College.objects.create(college_name=f"College {i}")
    colleges.append(c)

# Add 10 Programs
programs = []
for i in range(1, 11):
    # Distribute programs among colleges
    college = colleges[i % 8]
    p = Program.objects.create(prog_name=f"Program {i}", college=college)
    programs.append(p)

# Add 2 Organizations
orgs = []
for i in range(1, 3):
    o = Organization.objects.create(name=f"Org {i}", college=colleges[0], description=f"Description for Org {i}")
    orgs.append(o)

# Add 2 Students
students = []
for i in range(1, 3):
    s = Student.objects.create(
        student_id=f"2023-000{i}",
        lastname=f"Lastname{i}",
        firstname=f"Firstname{i}",
        program=programs[0]
    )
    students.append(s)

# Add 2 Organization Memberships
for i in range(0, 2):
    OrgMember.objects.create(
        student=students[i],
        organization=orgs[i],
        date_joined=date.today()
    )

print("Manual data entry simulated successfully.")
