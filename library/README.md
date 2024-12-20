# Library Management System

## Project Overview
A Flask-based Library Management System with CRUD operations for books and members.

## Prerequisites
- Python 3.8+
- Flask
- pytest

## Installation
1. Clone the repository
    -python -m venv venv
    -On Windows:
    venv\Scripts\activate
    -On macOS/Linux:
     source venv/bin/activate
2. Create a virtual environment (optional but recommended)
3. Install dependencies
-pip install -r requirements.txt



## API Endpoints

### **Books**

- `POST /books`: Add a new book.
- `GET /books`: List all books
- `GET /books/<id>`: Retrieve details of a specific book.
- `PUT /books/<id>`: Update a book's details.
- `DELETE /books/<id>`: Delete a book.

### **Members**

- `POST /members`: Add a new member.
- `GET /members`: List all members 
- `GET /members/<id>`: Retrieve details of a specific member.
- `PUT /members/<id>`: Update a member's details.
- `DELETE /members/<id>`: Delete a member.




## Run the application:

-python app.py
