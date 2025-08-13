# Student Portal

| A Django-based student portal application for managing announcements and stude | Variable           | Description                | Default |
| ------------------------------------------------------------------------------ | ------------------ | -------------------------- | ------- |
| `SECRET_KEY`                                                                   | Django secret key  | Required                   |
| `DEBUG`                                                                        | Debug mode         | `True`                     |
| `ALLOWED_HOSTS`                                                                | Allowed host names | `localhost,127.0.0.1`      |
| `DB_ENGINE`                                                                    | Database engine    | `django.db.backends.mysql` |
| `DB_NAME`                                                                      | Database name      | `student_portal_db`        |
| `DB_USER`                                                                      | Database user      | `root`                     |
| `DB_PASSWORD`                                                                  | Database password  | Required                   |
| `DB_HOST`                                                                      | Database host      | `localhost`                |
| `DB_PORT`                                                                      | Database port      | `3306`                     |

### Database

The project is configured to use **MySQL** as the primary database. You can also use SQLite for development or PostgreSQL for production.

#### MySQL Setup (Recommended)

1. **Install MySQL server:**

   ```bash
   sudo apt update
   sudo apt install mysql-server mysql-client libmysqlclient-dev
   ```

2. **Create the database:**

   ```bash
   sudo mysql -e "CREATE DATABASE student_portal_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
   ```

3. **Set MySQL root password:**

   ```bash
   sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'your_password'; FLUSH PRIVILEGES;"
   ```

4. **Update your .env file with MySQL credentials:**
   ```env
   DB_ENGINE=django.db.backends.mysql
   DB_NAME=student_portal_db
   DB_USER=root
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=3306
   ```

#### Alternative Database Configurations

**SQLite (Development only):**

```env
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

**PostgreSQL (Production recommended):**

````env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=student_portal_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```tion.

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
   git clone https://github.com/chihebabiza/Django_Student_Portal
   cd student_portal
````

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

| Variable        | Description        | Default               |
| --------------- | ------------------ | --------------------- |
| `SECRET_KEY`    | Django secret key  | Required              |
| `DEBUG`         | Debug mode         | `True`                |
| `ALLOWED_HOSTS` | Allowed host names | `localhost,127.0.0.1` |
| `DB_NAME`       | Database name      | `db.sqlite3`          |

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
