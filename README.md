# Little Lemon Restaurant API

Django REST API for restaurant management with JWT authentication and MySQL database.

## 🚀 Quick Installation

```bash
# Setup project
mkdir littlelemon-api && cd littlelemon-api
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install django djangorestframework djoser djangorestframework-simplejwt django-environ mysqlclient

# Create project
django-admin startproject littlelemon .
python manage.py startapp api
python manage.py startapp restaurant

# Setup MySQL
mysql -u root -p
CREATE DATABASE littlelemon;
CREATE USER 'littlelemon_user'@'localhost' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'littlelemon_user'@'localhost';
EXIT;

# Run migrations
python manage.py migrate
python manage.py makemigrations api
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## 📋 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/users/` | Register user |
| POST | `/api/token/` | Login (get JWT) |
| POST | `/api/token/refresh/` | Refresh token |

### Menu Items
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/menu-items/` | List menu items |
| POST | `/api/menu-items/` | Create menu item |
| GET | `/api/menu-items/{id}/` | Get menu item |
| PUT | `/api/menu-items/{id}/` | Update menu item |
| DELETE | `/api/menu-items/{id}/` | Delete menu item |

### Categories
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/categories/` | List categories |
| POST | `/api/categories/` | Create category |

### Bookings
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/bookings/` | List user bookings |
| POST | `/api/bookings/` | Create booking |
| GET | `/api/bookings/{id}/` | Get booking |
| PUT | `/api/bookings/{id}/` | Update booking |
| DELETE | `/api/bookings/{id}/` | Delete booking |

## 🔧 API Examples

### 1. Register User
```bash
POST /auth/users/
{
  "username": "testuser",
  "password": "testpass123", 
  "email": "test@example.com"
}
```

### 2. Login
```bash
POST /api/token/
{
  "username": "testuser",
  "password": "testpass123"
}

Response:
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 3. Get Menu Items
```bash
GET /api/menu-items/
Authorization: Bearer {access_token}

Response:
[
  {
    "id": 1,
    "title": "Bruschetta",
    "price": "12.99",
    "featured": true,
    "category": {
      "id": 1,
      "title": "Appetizers",
      "slug": "appetizers"
    },
    "description": ""
  }
]
```

### 4. Create Menu Item
```bash
POST /api/menu-items/
Authorization: Bearer {access_token}
{
  "title": "Pasta Carbonara",
  "price": "15.99",
  "featured": false,
  "category_id": 2,
  "description": "Classic Italian pasta"
}

Response:
{
  "id": 2,
  "title": "Pasta Carbonara",
  "price": "15.99",
  "featured": false,
  "category": {
    "id": 2,
    "title": "Main Courses",
    "slug": "main-courses"
  },
  "description": "Classic Italian pasta"
}
```

### 5. Get Categories
```bash
GET /api/categories/
Authorization: Bearer {access_token}

Response:
[
  {
    "id": 1,
    "title": "Appetizers",
    "slug": "appetizers"
  },
  {
    "id": 2,
    "title": "Main Courses", 
    "slug": "main-courses"
  }
]
```

### 6. Create Booking
```bash
POST /api/bookings/
Authorization: Bearer {access_token}
{
  "name": "John Doe",
  "no_of_guests": 4,
  "booking_date": "2025-06-01T18:00:00Z"
}

Response:
{
  "id": 1,
  "user": "testuser",
  "name": "John Doe",
  "no_of_guests": 4,
  "booking_date": "2025-06-01T18:00:00Z"
}
```

### 7. Get User Bookings
```bash
GET /api/bookings/
Authorization: Bearer {access_token}

Response:
[
  {
    "id": 1,
    "user": "testuser",
    "name": "John Doe", 
    "no_of_guests": 4,
    "booking_date": "2025-06-01T18:00:00Z"
  }
]
```

## 🔑 Authentication Required
All endpoints except registration and login require JWT token in header:
```
Authorization: Bearer {access_token}
```
