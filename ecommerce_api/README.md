E-commerce API
An advanced e-commerce API built with Django REST Framework, featuring user authentication, product management, order processing, caching with Redis, and real-time notifications using Django Channels.
Setup

Clone the Repository:
git clone https://github.com/yourusername/ecommerce_api.git
cd ecommerce_api


Create and Activate a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Set Up PostgreSQL Database:

Install PostgreSQL and ensure it’s running.
Create a database:CREATE DATABASE ecommerce_db;


Create a user and grant privileges:CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE ecommerce_db TO myuser;


Update ecommerce_api/settings.py with your database credentials if different.


Set Up Redis:

Install Redis and start the Redis server:redis-server


Ensure Redis is running on 127.0.0.1:6379.


Run Migrations:
python manage.py migrate


Create a Superuser:
python manage.py createsuperuser


Start the Development Server:
python manage.py runserver


WebSocket Notifications:

Connect a WebSocket client to ws://localhost:8000/ws/notifications/ with a valid JWT token to receive order status updates.



API Endpoints

Users:

POST /users/register/ - Register a new user
POST /users/token/ - Obtain JWT token
POST /users/token/refresh/ - Refresh JWT token
GET/PUT /users/profile/ - Retrieve or update user profile


Products:

GET /products/categories/ - List categories
POST/PUT/DELETE /products/categories/ - Admin manage categories
GET /products/products/ - List products (with pagination and filtering)
POST/PUT/DELETE /products/products/ - Admin manage products


Orders:

GET /orders/cart/ - View cart
POST /orders/cart/items/ - Add item to cart
PUT/DELETE /orders/cart/items/<item_id>/ - Update or remove cart item
POST /orders/place-order/ - Place an order
GET /orders/orders/ - View order history
PUT /orders/orders/<id>/ - Admin update order status



Notes

Replace 'your-secret-key-here' in settings.py with a secure key.
Ensure Redis and PostgreSQL are running before starting the server.
Use a tool like Postman to test API endpoints with JWT tokens.
