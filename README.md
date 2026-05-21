# PSUSphere

## Project Overview
PSUSphere is a modern, responsive web application built with Django for managing university student organizations, academic programs, and student directory records.

## Features
- **Interactive Dashboard**: Real-time statistics and summaries of organizations, students, and memberships.
- **Organization Management**: Track student organizations and their college affiliations.
- **Student Directory**: Comprehensive database of students across various programs.
- **Academic Structure**: Manage Colleges and degree Programs.
- **Membership Tracking**: Monitor student involvement in different organizations.
- **Enhanced Admin UI**: Custom administrative views for efficient data management.

## Technical Stack
- **Backend**: Django (Python)
- **Frontend**: Ready Bootstrap Dashboard Template
- **Database**: SQLite (Development)
- **Icons**: Line Awesome

## Project Structure
- `.gitignore`: Root-level version control configuration.
- `projectsite/`: Main Django project directory.
    - `studentorg/`: Core application containing models, views, and management commands.
    - `static/`: Consolidated Bootstrap theme assets (CSS, JS, Images).
    - `templates/`: Project-level HTML templates and UI components.
- `requirements.txt`: Python package dependencies.

## Setup & Execution
1. **Install Dependencies**: `pip install -r requirements.txt`
2. **Migrations**: `python manage.py migrate`
3. **Seed Data**: `python manage.py create_initial_data`
4. **Admin Account**: `python manage.py createsuperuser`
5. **Run Server**: `python manage.py runserver`

## Authors
- Developed as part of the PSUSphere Lab Project.
