# Phase-3-Mock-Code-Challenge-Theater-Work
```markdown
# Theater App

This module contains the core functionality for the Phase 3 Mock Code Challenge: Theater Work.

## Project Structure

- **models.py**: Defines SQLAlchemy models for the database.
- **seed.py**: Seeds the database with sample data.
- **main.py**: Main application entry point.

## Models

- **Audition**: Represents an audition with actor details, location, and role association.
- **Role**: Represents a role with a character name.

## Usage

### Creating Database Migrations

```bash
alembic revision --autogenerate -m "your_migration_message"
Applying Migrations

alembic upgrade head
Seeding the Database

python lib/seed.py
Running the Application

python lib/main.py
Testing
To run tests, use:


pytest

License
This project is licensed under the Unlicense, making it free and unencumbered software.


Feel free to adapt and modify these READMEs based on the specifics of your project.