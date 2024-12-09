from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    publication_year: int
    id: Optional[int] = None

    def to_dict(self):
        return asdict(self)

@dataclass
class Member:
    name: str
    email: str
    id: Optional[int] = None

    def to_dict(self):
        return asdict(self)
