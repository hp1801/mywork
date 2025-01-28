from typing import List, Optional, Dict
from models import Book, Member

class Database:
    def __init__(self):
        self._books: Dict[int, Book] = {}
        self._members: Dict[int, Member] = {}
        self._book_id_counter = 1
        self._member_id_counter = 1

    def add_book(self, book: Book) -> Book:
        book.id = self._book_id_counter
        self._books[self._book_id_counter] = book
        self._book_id_counter += 1
        return book

    def get_book(self, book_id: int) -> Optional[Book]:
        return self._books.get(book_id)

    def update_book(self, book_id: int, book_data: Dict) -> Optional[Book]:
        if book_id not in self._books:
            return None
        book = self._books[book_id]
        for key, value in book_data.items():
            if hasattr(book, key):
                setattr(book, key, value)
        return book

    def delete_book(self, book_id: int) -> bool:
        return self._books.pop(book_id, None) is not None

    def search_books(self, query: str) -> List[Book]:
        if not query:
            return list(self._books.values())
        return [
            book for book in self._books.values()
            if query.lower() in book.title.lower() or query.lower() in book.author.lower()
        ]

    def add_member(self, member: Member) -> Member:
        member.id = self._member_id_counter
        self._members[self._member_id_counter] = member
        self._member_id_counter += 1
        return member

    def get_member(self, member_id: int) -> Optional[Member]:
        return self._members.get(member_id)

    def update_member(self, member_id: int, member_data: Dict) -> Optional[Member]:
        if member_id not in self._members:
            return None
        member = self._members[member_id]
        for key, value in member_data.items():
            if hasattr(member, key):
                setattr(member, key, value)
        return member

    def delete_member(self, member_id: int) -> bool:
        return self._members.pop(member_id, None) is not None

    def list_members(self) -> List[Member]:
        return list(self._members.values())
