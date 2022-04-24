import os
import django
from vacancies.models import Company, Specialty, Vacancy
import data

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "stepik_find.settings")
django.setup()

for i in data.specialties:
    Specialty.objects.create(
        code=i.get('code'),
        title=i.get('title'),
        picture=f"/static/specialties/specty_{i.get('code')}.png"
        ).save()

for i in data.companies:
    Company.objects.create(
        name=i.get('title'),
        location=i.get('location'),
        logo=f"/static/{i.get('logo')}",
        description=i.get('description'),
        employee_count=i.get('employee_count'),
        ).save()

for i in data.jobs:
    specialty = Specialty.objects.get(code=i.get('specialty'))
    company = Company.objects.get(id=i.get('company'))

    Vacancy.objects.create(
        title=i.get('title'),
        specialty=specialty,
        company=company,
        skills=i.get('skills'),
        description=i.get('description'),
        salary_min=i.get('salary_from'),
        salary_max=i.get('salary_to'),
        published_at=i.get('posted'),
        ).save()
