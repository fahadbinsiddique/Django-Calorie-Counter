# 🥗 Calorie Tracker — Django Web Application

A simple yet functional **Calorie Tracking Web Application** built with Django. Users can register, set up their health profile, log daily food intake, and track how many calories they have consumed versus their daily calorie requirement (BMR).

---

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Database Models](#database-models)
- [BMR Calculation](#bmr-calculation)
- [URL Routes](#url-routes)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Known Issues](#known-issues)
- [Future Improvements](#future-improvements)

---

## ✨ Features

- **User Registration & Authentication** — Secure sign-up, login, and logout using Django's built-in auth system.
- **User Profile Management** — Each user can save personal details (name, age, height, weight, gender).
- **Automatic BMR Calculation** — Basal Metabolic Rate (BMR) is automatically calculated based on the user's profile data using the Harris-Benedict equation.
- **Daily Calorie Logging** — Users can log food items with their calorie values throughout the day.
- **Dashboard Overview** — The dashboard shows total calories consumed today and how many more calories the user still needs to meet their daily BMR goal.
- **Login-Protected Pages** — Dashboard, profile, and calorie logging pages are protected with `@login_required`.

---

## 🛠 Tech Stack

| Layer        | Technology                     |
|--------------|--------------------------------|
| Backend      | Python 3, Django               |
| Database     | SQLite3 (default)              |
| Frontend     | Django Templates, Bootstrap    |
| Auth         | Django Built-in Auth System    |

---

## 📁 Project Structure

```
calorie_project/
│
├── calorie_app/                  # Main application
│   ├── migrations/               # Database migrations
│   ├── templates/
│   │   ├── master/
│   │   │   ├── base.html         # Base layout template
│   │   │   ├── base_form.html    # Reusable form template
│   │   │   └── nav.html          # Navigation bar
│   │   ├── dashboard.html        # Dashboard page
│   │   └── profile.html          # Profile page
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                  # Django forms
│   ├── models.py                 # Database models
│   ├── urls.py                   # App-level URL patterns
│   └── views.py                  # View logic
│
├── calorie_project/              # Project configuration
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── db.sqlite3                    # SQLite database
└── manage.py
```

---

## 🗄 Database Models

### `ProfileModel`
Stores the user's personal health information.

| Field    | Type                 | Description                     |
|----------|----------------------|---------------------------------|
| `user`   | OneToOneField        | Linked to Django's `User` model |
| `name`   | CharField            | Full name of the user           |
| `age`    | PositiveIntegerField | Age in years                    |
| `height` | FloatField           | Height in centimeters (cm)      |
| `weight` | FloatField           | Weight in kilograms (kg)        |
| `gender` | CharField            | `Male` or `Female`              |
| `bmr`    | FloatField           | Auto-calculated BMR value (kcal)|

### `CalorieConsumeModel`
Logs each food item a user eats.

| Field             | Type       | Description                            |
|-------------------|------------|----------------------------------------|
| `user`            | ForeignKey | Linked to Django's `User` model        |
| `item_name`       | CharField  | Name of the food item                  |
| `calorie_consume` | FloatField | Calories in the food item (kcal)       |
| `created_add`     | DateField  | Auto-set to the date entry is created  |

---

## 🔢 BMR Calculation

The app uses the **Harris-Benedict Equation** to calculate daily calorie needs:

**For Males:**
```
BMR = 66.47 + (13.75 × weight in kg) + (5.003 × height in cm) − (6.755 × age in years)
```

**For Females:**
```
BMR = 655.1 + (9.563 × weight in kg) + (1.850 × height in cm) − (4.676 × age in years)
```

This value is saved in the `ProfileModel.bmr` field upon profile update.

---

## 🔗 URL Routes

| URL                 | View Function    | Name             | Description                     |
|---------------------|------------------|------------------|---------------------------------|
| `/`                 | `register_page`  | `register_page`  | User registration page          |
| `/login/`           | `login_page`     | `login_page`     | User login page                 |
| `/logout/`          | `logout_page`    | `logout_page`    | Logs out the current user       |
| `/dashboard/`       | `dashboard`      | `dashboard`      | Shows daily calorie summary     |
| `/profile/`         | `profile`        | `profile`        | View user profile and BMR       |
| `/profile-update/`  | `profile_update` | `profile_update` | Update profile & recalculate BMR|
| `/Calorie-Consume/` | `CalorieConsume` | `CalorieConsume` | Log a new food item             |

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Steps

**1. Clone or extract the project:**
```bash
unzip calorie_project.zip
cd calorie_project
```

**2. Create and activate a virtual environment:**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

**3. Install Django:**
```bash
pip install django
```

**4. Apply database migrations:**
```bash
python manage.py migrate
```

**5. (Optional) Create a superuser for the admin panel:**
```bash
python manage.py createsuperuser
```

**6. Run the development server:**
```bash
python manage.py runserver
```

**7. Open in browser:**
```
http://127.0.0.1:8000/
```

---

## 📖 Usage Guide

1. **Register** — Go to `/` and create a new account.
2. **Login** — Log in with your credentials at `/login/`.
3. **Update Profile** — Go to `/profile-update/` and enter your name, age, height, weight, and gender. Your BMR will be calculated and saved automatically.
4. **Log Food** — Go to `/Calorie-Consume/` to add a food item with its calorie value.
5. **Check Dashboard** — Visit `/dashboard/` to see:
   - Total calories consumed today
   - Remaining calories needed to meet your BMR goal


## 🚀 Future Improvements

- [ ] Fix the dashboard BMR variable bug
- [ ] Add calorie history with date filtering
- [ ] Integrate a food database API (e.g., USDA FoodData Central) for automatic calorie lookup
- [ ] Add activity level multipliers (TDEE calculation)
- [ ] Add visual charts for calorie progress tracking
- [ ] Improve UI with a polished Bootstrap theme
- [ ] Add REST API support using Django REST Framework
- [ ] Write unit tests for views and BMR logic
- [ ] Add Docker support for easy deployment

---

## 👤 Author

> This project was built as a Django learning project focused on user authentication, model relationships, and form handling.

---

## 📄 License

This project is open-source and free to use for educational purposes.
