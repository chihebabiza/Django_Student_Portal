# Student Portal

A Django-based student portal application for managing announcements and student information.

## Features

- 📢 **Announcements System**: View and manage announcements by category
- 🎓 **Student Management**: Handle student information and data
- 🔐 **Authentication**: User login and authentication system
- 📱 **Responsive Design**: Mobile-friendly interface with Tailwind CSS
- ⚡ **Modern UI**: Clean and intuitive user interface

## Prerequisites

- Python 3.8+
- Django 4.2+
- Virtual environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd student_portal
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file and update the following:
   - `SECRET_KEY`: Generate a new Django secret key
   - `DEBUG`: Set to `False` for production
   - `ALLOWED_HOSTS`: Add your domain names for production

5. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## Project Structure

```
student_portal/
├── apps/                      # Django applications
│   ├── administration/        # Admin functionality
│   ├── announcements/         # Announcements management
│   ├── authentication/        # User authentication
│   ├── projects/             # Projects management
│   └── students/             # Student management
├── static/                   # Static files (CSS, JS, images)
├── templates/                # HTML templates
│   ├── partials/            # Reusable template components
│   └── student/             # Student-specific templates
├── student_portal/          # Main project settings
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── .env.example           # Environment variables template
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | Required |
| `DEBUG` | Debug mode | `True` |
| `ALLOWED_HOSTS` | Allowed host names | `localhost,127.0.0.1` |
| `DB_NAME` | Database name | `db.sqlite3` |

### Database

The project uses SQLite by default. For production, you can configure PostgreSQL or MySQL by updating the database settings in `settings.py` and the corresponding environment variables.

## Apps Description

- **Administration**: Admin panel functionality and administrative features
- **Announcements**: Create, read, update, and delete announcements with category filtering
- **Authentication**: User registration, login, logout, and session management
- **Projects**: Project management and tracking
- **Students**: Student information and profile management

## Usage

### Viewing Announcements

1. Navigate to the home page
2. Use filter buttons to view announcements by category:
   - General
   - Computer Science
   - Mathematics
   - Physics
   - Chemistry

### Admin Features

If you have admin privileges:
1. Log in to the admin panel at `/admin/`
2. Create and manage announcements
3. Manage user accounts and permissions

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Security

- Never commit the `.env` file to version control
- Always use environment variables for sensitive data
- Set `DEBUG=False` in production
- Use strong, unique secret keys
- Keep dependencies updated

## Deployment

For production deployment:

1. Set environment variables:
   ```bash
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com
   SECRET_KEY=your-production-secret-key
   ```

2. Configure a production database (PostgreSQL recommended)

3. Set up static file serving:
   ```bash
   python manage.py collectstatic
   ```

4. Use a production WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn student_portal.wsgi:application
   ```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
