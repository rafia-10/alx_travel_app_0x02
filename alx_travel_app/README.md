# alx_travel_app_0x01
🚀 ALX Travel App
Welcome to ALX Travel App, a Django-based backend system designed for managing travel listings and bookings. This app is built as part of an ALX backend milestone project.

🌟 Features
🏨 Manage travel Listings (CRUD)

📅 Manage Bookings (CRUD)

⭐ Manage Reviews

💥 RESTful APIs using Django REST Framework

🛡️ Swagger & Redoc API documentation

✅ CORS support for cross-origin requests

💾 MySQL database integration

🥕 Seeder script to populate sample data

💻 Tech Stack
Backend: Django, Django REST Framework

Database: MySQL

Documentation: Swagger (drf-yasg), Redoc

Others: Celery, RabbitMQ (for future tasks)

⚙️ Installation
bash
Copy
Edit
# Clone the repository
git clone https://github.com/rafia-10/alx_travel_app_0x01.git
cd alx_travel_app_0x01

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
🗄️ Database Setup
Make sure MySQL is installed and running.

Create your database:

sql
Copy
Edit
CREATE DATABASE alx_travel_app_db;
Update your .env file with your DB credentials:

bash
Copy
Edit
DATABASE_URL=mysql://root:yourpassword@localhost:3306/alx_travel_app_db
🔥 Running the App
bash
Copy
Edit
# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Seed sample data (optional)
python manage.py seed

# Run the server
python manage.py runserver
📄 API Documentation
After running the server, access the docs:

Swagger UI: http://127.0.0.1:8000/swagger/

Redoc: http://127.0.0.1:8000/redoc/

🚥 API Endpoints
Method	Endpoint	Description
GET/POST	/api/listings/	List or create listings
GET/PUT/DELETE	/api/listings/{id}/	Retrieve, update or delete listing
GET/POST	/api/bookings/	List or create bookings
GET/PUT/DELETE	/api/bookings/{id}/	Retrieve, update or delete booking

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

💌 Contact
Author: Rafia Kedir

Email: rafiakedir22@gmail.com

LinkedIn: Rafia Kedir

⭐ License
This project is licensed under the BSD License.

✨ Happy hacking, and may your bugs be minimal! ✨
