# sienge-dashboad
This Project We gonna created project with more labery! 

sienge-dashboard/
├── .env
├── .gitignore
├── requirements.txt
├── manage.py
├── core/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── __init__.py
│   ├── dashboard/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── templates/
│   │       └── dashboard/
│   └── sienge_integration/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── services/
│       │   ├── __init__.py
│       │   └── client.py
│       └── utils.py
├── templates/
│   ├── base.html
│   └── includes/
└── static/
    ├── css/
    ├── js/
    └── img/
