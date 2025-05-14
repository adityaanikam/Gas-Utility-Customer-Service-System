# Gas Utility Customer Service System

A Django-based web application for managing gas utility customer service requests. This system allows customers to submit service requests, track their status, and communicate with customer service representatives.

## Features

- Customer service request submission and tracking
- File attachments for service requests
- Staff dashboard for managing requests
- Customer profiles with 10-digit phone validation
- Request notes and updates
- Priority-based request management
- Responsive design with Bootstrap 5
- User registration from the frontend
- Secure logout (POST only)

## Requirements

- Python 3.8+
- Django 4.2+
- Pillow
- django-crispy-forms
- crispy-bootstrap5

## Installation

1. Clone the repository:
```bash
git clone https://github.com/adityaanikam/Gas-Utility-Customer-Service-System.git
git checkout main
cd Gas-Utility-Customer-Service-System
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Usage

- Access the admin interface at `http://localhost:8000/admin` to manage users and service requests.
- Customers can access the system at `http://localhost:8000` to submit and track service requests.
- Staff members can access the staff dashboard at `http://localhost:8000/staff/` to manage requests.
- Register a new user at `/register/` or via the "Register" link in the navbar.
- Logout securely using the POST logout button in the navbar.

## Project Structure

```
gas_utility/
├── customer_services/
│   ├── models.py      # Database models
│   ├── views.py       # View functions
│   ├── forms.py       # Form definitions
│   └── urls.py        # URL routing
├── templates/
│   ├── base.html      # Base template
│   ├── registration/
│   │   ├── login.html
│   │   ├── register.html
│   │   └── logged_out.html
│   └── customer_services/
│       ├── dashboard.html
│       ├── create_request.html
│       ├── request_detail.html
│       ├── update_request.html
│       ├── staff_dashboard.html
│       └── profile.html
├── static/
│   ├── css/
│   └── js/
└── media/
    └── request_attachments/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Repository:** [Gas-Utility-Customer-Service-System](https://github.com/adityaanikam/Gas-Utility-Customer-Service-System.git) 