import json
from typing import Dict, List, Optional
from flask import Flask, request, jsonify
from models import Book, Member
from database import Database

app = Flask(__name__)
db = Database()

# Preload some data
db.add_book(Book(title="1984", author="George Orwell", isbn="1234567890", publication_year=1949))
db.add_book(Book(title="To Kill a Mockingbird", author="Harper Lee", isbn="9876543210", publication_year=1960))
db.add_member(Member(name="John Doe", email="john.doe@example.com"))
db.add_member(Member(name="Jane Smith", email="jane.smith@example.com"))

# Book Routes
@app.route('/books', methods=['POST'])
def create_book():
    book_data = request.json
    book = Book(**book_data)
    db.add_book(book)
    return jsonify(book.to_dict()), 201

@app.route('/books', methods=['GET'])
def list_books():
    books = db.search_books(query="")
    return jsonify([book.to_dict() for book in books])

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id: int):
    book = db.get_book(book_id)
    if book:
        return jsonify(book.to_dict())
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id: int):
    book_data = request.json
    updated_book = db.update_book(book_id, book_data)
    if updated_book:
        return jsonify(updated_book.to_dict())
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id: int):
    if db.delete_book(book_id):
        return '', 204
    return jsonify({"error": "Book not found"}), 404

# Member Routes
@app.route('/members', methods=['POST'])
def create_member():
    member_data = request.json
    member = Member(**member_data)
    db.add_member(member)
    return jsonify(member.to_dict()), 201

@app.route('/members', methods=['GET'])
def list_members():
    members = db.list_members()
    return jsonify([member.to_dict() for member in members])

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id: int):
    member = db.get_member(member_id)
    if member:
        return jsonify(member.to_dict())
    return jsonify({"error": "Member not found"}), 404

@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id: int):
    member_data = request.json
    updated_member = db.update_member(member_id, member_data)
    if updated_member:
        return jsonify(updated_member.to_dict())
    return jsonify({"error": "Member not found"}), 404

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id: int):
    if db.delete_member(member_id):
        return '', 204
    return jsonify({"error": "Member not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
