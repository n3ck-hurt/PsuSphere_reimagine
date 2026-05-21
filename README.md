# PSUSphere

## Project Description
PSUSphere is a Django-based web application designed to manage student organizations, colleges, and programs within a university setting. It provides a robust administrative interface for tracking students, their affiliations with various organizations, and the academic structure of the institution.

## Key Functionality
- **College Management**: Track different colleges within the university.
- **Program Management**: Manage academic programs and their association with colleges.
- **Organization Tracking**: Maintain a list of student organizations and their details.
- **Student Database**: Store student information including their enrolled programs.
- **Membership Management**: Track student memberships in various organizations, including the date they joined.
- **Automated Seeding**: Includes a management command to populate the database with realistic fake data for testing and development.
- **Enhanced Admin Dashboard**: Custom administrative views for better data visibility and searchability.

## Authors / Team Details
- Developed as part of the PSUSphere Project.
- Team: [Author Names]

## Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run migrations: `python manage.py migrate`.
4. Create a superuser: `python manage.py createsuperuser`.
5. Run the server: `python manage.py runserver`.
6. (Optional) Seed initial data: `python manage.py create_initial_data`.
