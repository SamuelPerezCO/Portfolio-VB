# 🚀 Django Personal Portfolio

A clean, dark-themed personal portfolio built with Django — featuring a projects showcase, skills display, work timeline, and contact form.

## Features

- **Home** — Hero section, skills by category with animated bars, featured projects
- **About** — Bio, work experience & education timeline, CV download
- **Projects** — Filterable project grid with detail pages
- **Contact** — Contact form that saves messages to the DB and can send email notifications
- **Admin** — Full Django admin to manage all content
- **Demo data** — Fixtures to pre-populate the site instantly

## Tech Stack

- **Backend**: Django 4.2, Django REST Framework ready
- **Frontend**: Bootstrap 5, custom CSS (dark editorial theme), vanilla JS
- **Storage**: WhiteNoise for static files, Pillow for images
- **Forms**: django-crispy-forms + crispy-bootstrap5
- **Config**: python-dotenv for environment variables

---

## Quick Start

### 1. Clone & set up the environment

```bash
git clone <your-repo-url>
cd django_portfolio

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure environment variables

```bash
cp .env.example .env
# Edit .env with your SECRET_KEY and optional email settings
```

Generate a secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 3. Run migrations and load demo data

```bash
python manage.py migrate
python manage.py loaddata portfolio/fixtures/initial_data.json
```

### 4. Create a superuser (for the admin panel)

```bash
python manage.py createsuperuser
```

### 5. Run the development server

```bash
python manage.py runserver
```

Visit:
- **Site** → http://127.0.0.1:8000/
- **Admin** → http://127.0.0.1:8000/admin/

---

## Project Structure

```
django_portfolio/
├── config/                  # Django project settings & URLs
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── portfolio/               # Main app
│   ├── migrations/
│   ├── static/portfolio/
│   │   ├── css/main.css
│   │   └── js/main.js
│   ├── templates/portfolio/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── projects.html
│   │   ├── project_detail.html
│   │   └── contact.html
│   ├── fixtures/
│   │   └── initial_data.json
│   ├── models.py            # Profile, Project, Skill, Experience, ContactMessage
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── media/                   # User-uploaded files (created at runtime)
├── staticfiles/             # Collected static files (created at runtime)
├── manage.py
├── requirements.txt
└── .env.example
```

---

## Customizing Content

All content is managed through the **Django Admin** at `/admin/`:

| Section | What to edit |
|---|---|
| **Profile** | Your name, bio, avatar, social links, CV |
| **Skills** | Tech stack with categories and proficiency % |
| **Projects** | Title, description, images, links, technologies |
| **Experience** | Work history and education entries |
| **Contact Messages** | View incoming messages from the contact form |

---

## Deployment (Production)

1. Set `DEBUG=False` in `.env`
2. Set `ALLOWED_HOSTS` to your domain
3. Generate a strong `SECRET_KEY`
4. Run `python manage.py collectstatic`
5. Configure a production database (PostgreSQL recommended)
6. Set up email credentials for contact form notifications
7. Use Gunicorn + Nginx or a PaaS like Railway, Render, or Fly.io

---

## License

MIT — feel free to use this as your own portfolio base.
# Portfolio-VB
