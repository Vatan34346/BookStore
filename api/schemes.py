from pydantic import BaseModel

# User


class User(BaseModel):
    id: int
    email: str
    name: str


class UserRegister(BaseModel):
    email: str
    password: str
    name: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserUpdate(BaseModel):
    email: str
    password: str
    name: str

# Author


class Author(BaseModel):
    id: int
    author_name: str


class AuthorUpdateCreate(BaseModel):
    author_name: str


# Genres


class Genre(BaseModel):
    id: int
    genre_name: str


class GenreUpdateCreate(BaseModel):
    genre_name: str


# conditions


class Condition(BaseModel):
    id: int
    condition_name: str


class ConditionUpdateCreate(BaseModel):
    condition_name: str

# contacts


class Coordinates(BaseModel):
    lat: int
    log: int


class Contact(BaseModel):
    id: int
    address: str
    phone: str
    coordinates: str


class ContactUpdateCreate(BaseModel):
    address: str
    phone: str
    coordinates: Coordinates

# books


class BookFilters(BaseModel):
    authors_id: int
    genres_id: int
    conditions_id: int
    contacts_id: int
    users_id: int


class BookUpdateCreate(BaseModel):
    book_title: str
    book_description: str
    authors_id: int
    genres_id: int
    conditions_id: int
    contacts_id: int
    users_id: int
    listOfInterestedUsers: str
