# CarpetAccounting API

The **Accounting API** is a backend project developed with **Django Rest Framework (DRF)** to manage users and carpets for a workshop. This API is fully built with class-based views, providing a structured and scalable approach to handle core functionalities.

## Features

- **Carpet Management**:
  - Add, update, view, and delete carpet details.
  - Store basic information like type, size, and design.

- **User Management**:
  - Add, update, view, and delete user details.

- **Authentication**:
  - Login functionality using JWT for secure access.

- **Custom Management Command**:
  - Import bulk carpet data into the database from JSON files using a custom management command.
  - python manage.py import_carpet_data --file jsonfilename.json


## Tech Stack

- **Backend Framework**: Django 4.x, Django Rest Framework (DRF)
- **Database**: SQLite3 (default Django database)
- **Architecture**: Class-Based Views

## Installation

### Prerequisites
- Python 3.8 or above
- Virtual environment manager (e.g., venv or pipenv)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/accounting.git
   cd accounting
