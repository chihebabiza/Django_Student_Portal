# Django Student Portal

A modern Django-based student portal application for managing announcements and educational content across different academic departments.

## 🚀 Features

- 📢 **Dynamic Announcements System**: Create, view, and manage announcements with departmental filtering
- 🏷️ **Category-based Organization**: Filter announcements by department (General, Computer Science, Physics, Chemistry, Mathematics)
- 🔧 **Admin Interface**: Full CRUD operations for announcements through Django admin
- 🗄️ **Flexible Database Support**: Configured for MySQL with SQLite fallback
- 📱 **Responsive Design**: Clean and modern user interface
- ⚙️ **Environment Configuration**: Secure configuration management with environment variables

## 🛠️ Technology Stack

- **Backend**: Django 5.2.5
- **Database**: MySQL (primary), SQLite (development)
- **Environment Management**: python-dotenv
- **Frontend**: HTML templates with responsive design

## 📋 Prerequisites

- Python 3.8+
- MySQL Server (for production) or SQLite (for development)
- Virtual environment (recommended)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/chihebabiza/Django_Student_Portal.git
cd student_portal
```

### 2. Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Database Setup

#### Option A: MySQL (Recommended for Production)

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

#### Option B: SQLite (Quick Development Setup)

No additional setup required - SQLite database will be created automatically.

### 5. Environment Configuration

Create a `.env` file in the project root:

```env
# Security
SECRET_KEY="your-secret-key-here"
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# MySQL Database Configuration
DB_ENGINE=django.db.backends.mysql
DB_NAME=student_portal_db
DB_USER=root
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=3306

# Alternative SQLite Configuration (uncomment to use)
# DB_ENGINE=django.db.backends.sqlite3
# DB_NAME=db.sqlite3
```

### 6. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 8. Start Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
student_portal/
├── apps/                      # Django applications
│   ├── administration/        # Admin functionality
│   ├── announcements/         # Announcements CRUD operations
│   ├── authentication/        # User authentication (future)
│   ├── projects/             # Projects management (future)
│   └── students/             # Student management (future)
├── static/                   # Static files (CSS, JS, images)
│   └── js/
│       └── script.js         # JavaScript functionality
├── templates/                # HTML templates
│   ├── partials/            # Reusable components
│   │   ├── head.html        # HTML head section
│   │   ├── navbar.html      # Navigation bar
│   │   └── footer.html      # Footer
│   ├── student/             # Student-specific templates
│   ├── index.html           # Main announcements page
│   ├── login.html           # Login page
│   ├── 404.html             # Error pages
│   └── error.html
├── student_portal/          # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI configuration
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── .env                   # Environment variables
```

## ⚙️ Configuration

### Environment Variables

| Variable        | Description        | Default                    |
| --------------- | ------------------ | -------------------------- |
| `SECRET_KEY`    | Django secret key  | Required                   |
| `DEBUG`         | Debug mode         | `True`                     |
| `ALLOWED_HOSTS` | Allowed host names | `localhost,127.0.0.1`      |
| `DB_ENGINE`     | Database engine    | `django.db.backends.mysql` |
| `DB_NAME`       | Database name      | `student_portal_db`        |
| `DB_USER`       | Database user      | `root`                     |
| `DB_PASSWORD`   | Database password  | Required                   |
| `DB_HOST`       | Database host      | `localhost`                |
| `DB_PORT`       | Database port      | `3306`                     |

## 📱 Usage

### Viewing Announcements

1. Navigate to the home page at `http://127.0.0.1:8000/`
2. View all announcements or filter by category:
   - General
   - Computer Science
   - Physics
   - Chemistry
   - Mathematics

### Managing Announcements (Admin)

1. Access the admin panel at `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Navigate to "Announcements" to create, edit, or delete announcements
4. Each announcement includes:
   - Title
   - Content
   - Category/Display type
   - Date and time

## 🔧 Development

### App Descriptions

- **announcements**: Core functionality for announcement management with CRUD operations
- **administration**: Administrative features and utilities
- **authentication**: User authentication system (planned)
- **projects**: Project management features (planned)
- **students**: Student information management (planned)

### Current Implementation Status

✅ **Completed:**

- Announcements CRUD operations
- Category-based filtering
- MySQL/SQLite database configuration
- Admin interface integration
- Responsive template structure

🚧 **In Development:**

- User authentication system
- Student management features
- Project management functionality

## 🚀 Deployment

### Production Deployment

1. **Environment Configuration:**

   ```env
   DEBUG=False
   ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
   SECRET_KEY=your-production-secret-key
   ```

2. **Database Setup:**
   Configure a production database (MySQL or PostgreSQL recommended)

3. **Static Files:**

   ```bash
   python manage.py collectstatic
   ```

4. **WSGI Server:**
   ```bash
   pip install gunicorn
   gunicorn student_portal.wsgi:application
   ```

### Security Considerations

- 🔒 Keep `SECRET_KEY` secure and unique
- 🚫 Never commit `.env` files to version control
- 🔧 Set `DEBUG=False` in production
- 🔄 Keep dependencies updated regularly
- 🌐 Configure proper `ALLOWED_HOSTS` for production

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

- Open an issue on [GitHub](https://github.com/chihebabiza/Django_Student_Portal/issues)
- Check the Django documentation for general Django-related questions
- Review the configuration section for environment setup issues

## 📊 Project Status

This project is actively maintained and under development. Current focus areas include expanding the authentication system and adding comprehensive student management features.
