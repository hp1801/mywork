# Gas Utility Portal

This project is a Django-based web application for managing customer accounts and service requests in a gas utility company. It includes customer registration, login/logout functionality, profile management, service request submission, and tracking.

## Features

User Authentication

1.-User registration with account details (account number, contact number, address).

-Login and logout functionality.

-Admin-only views for managing customer requests.

2.Customer Profile

-Customers can view their account details and profile information.

3.Service Management

-Customers can submit service requests (e.g., repairs, installations, billing issues).

-Customers can track the status of their requests.

4.Admin Dashboard

-Admins can view and manage all service requests.

## Installation

```python
#Clone the Repository
git clone <repository_url>
cd gas_project
```
```python
#Set Up Virtual Environment
python -m venv venv
source venv/bin/activate
```
```python
#Migrate the Database
python manage.py makemigrations
python manage.py migrate
```
```python
#Run the Server
python manage.py runserver
```
```python
#Create a Superuser (Admin Access)
python manage.py createsuperuser
```
Access the App:

Admin Panel: http://127.0.0.1:8000/admin

App Home: http://127.0.0.1:8000

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

